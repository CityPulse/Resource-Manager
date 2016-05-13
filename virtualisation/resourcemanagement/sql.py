from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.log import Log as L
import os
import psycopg2
import datetime

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class SQL(object):
    datatype_map = {'int': 'INT', 'str': 'VARCHAR', 'float': 'FLOAT', 'datetime.datetime': 'TIMESTAMP'}
    escape_string = ('str', 'datetime.datetime')
    cp_observation_fields = ["sampling_time", "sensor_uuid", "observation_uuid", "data", "quality"]
    SCHEMA = "observations"# + ("_dev" if os.environ['LOGNAME'] == 'mafi' else "")

    def __init__(self, gdi_config, rm):
        self.rm = rm
        connect_str = "host='%s' dbname='%s' user='%s' password='%s' port=%d" % (
            gdi_config.host, gdi_config.database, gdi_config.username, gdi_config.password, gdi_config.port)
        self.conn = psycopg2.connect(connect_str)
        self.curs = self.conn.cursor()
        try:
            self.curs.execute("CREATE SCHEMA IF NOT EXISTS %s;" % SQL.SCHEMA)
            # self.curs.execute("CREATE TABLE IF NOT EXISTS %s.cp_sensors (sensor_uuid UUID CONSTRAINT uuid_key PRIMARY KEY, sensor_annotation_id VARCHAR, sercvice_category VARCHAR, traffic INTEGER, geom GEOMETRY(GEOMETRY, 4326) );" % (SQL.SCHEMA,))
            self.curs.execute("CREATE TABLE IF NOT EXISTS %s.cp_sensors (sensor_uuid UUID CONSTRAINT uuid_key PRIMARY KEY, sensor_annotation_id VARCHAR, sercvice_category VARCHAR, traffic INTEGER, geom GEOMETRY(GEOMETRY, 4326) );" % ("public",))
            cols = ["sampling_time TIMESTAMP", "sensor_uuid UUID", "observation_uuid UUID", "data JSON", "quality JSON"]
            query = 'CREATE TABLE IF NOT EXISTS %s.cp_observations ( %s, PRIMARY KEY (%s), FOREIGN KEY (sensor_uuid) REFERENCES %s.cp_sensors(sensor_uuid));\n' % (SQL.SCHEMA, ', '.join(cols),  ", ".join(["observation_uuid"]), "public")
            self.curs.execute(query)

            # index over sampling_time and sensor_uuid
            # since a 'IF NOT EXISTS' is not available for us (version < 9.5)
            # the error is catched in a separate try-catch
            try:
                query = 'CREATE INDEX "timeindex" ON %s.cp_observations USING btree (sampling_time);' % (SQL.SCHEMA,)
                self.curs.execute(query)
                query = 'CREATE INDEX uuidindex ON %s.cp_observations USING btree (sensor_uuid);' % (SQL.SCHEMA,)
                self.curs.execute(query)
            except:
                pass

            # primary secondary observation_uuid map
            query = 'CREATE TABLE IF NOT EXISTS %s.p_s_observation_uuid (main UUID, secondary UUID);' % (SQL.SCHEMA,)
            self.curs.execute(query)

            self.conn.commit()
            L.i("SQL: schema/tables created")
        except Exception as e:
            L.e("SQL: Could not create schema/tables", e)
            self.conn.rollback()

    def is_timestamp_field(self, fieldname, sd):
        return sd.isTimestampedStream() and sd.timestamp.inField == fieldname

    def insert_observation(self, sd, ob, q):
        # L.d("Inserting observation", ob)
        query = None
        try:
            _ob = ob.deepcopy()
            _ob.fields = filter(lambda x: not self.is_timestamp_field(x, sd), ob.fields)
            if sd.isTimestampedStream() and sd.timestamp.inField in _ob:
                _ob.remove_item(sd.timestamp.inField)
            if 'latency' in _ob:
                _ob.remove_item('latency')
            primary_ob_uuid = None
            p_s_values = []
            for _f in ob.fields:
                if _f not in ob or (sd.isTimestampedStream() and sd.timestamp.inField == _f):
                    continue
                if not query:
                    field = ob[_f]
                    primary_ob_uuid = self._escape_string(None, str(field.observationID))
                    v = [
                        "TIMESTAMP " + self._escape_string(None, field.observationSamplingTime),
                        self._escape_string(None, str(sd.uuid)),
                        primary_ob_uuid,
                        self._escape_string(None, _ob.dumps(), singleqoute_to_double=True),
                        self._escape_string(None, JOb(q).dumps())
                    ]
                    query = "INSERT INTO %s.cp_observations (%s) VALUES (%s);\n" % (SQL.SCHEMA, ','.join(SQL.cp_observation_fields), ','.join(v))
                    del v
                p_s_values.append("(%s, %s)" % (primary_ob_uuid, self._escape_string(None, str(field.observationID))))
            if query:
                query += "INSERT INTO %s.p_s_observation_uuid (main, secondary) VALUES %s;\n" % (SQL.SCHEMA, ','.join(p_s_values))
            L.d2("Using query:", query)

            if query:
                self.curs.execute(query)
                self.conn.commit()
                del query
                del _ob
            return True
        except Exception as e:
            self.conn.rollback()
            L.e(e)
            L.e("SQL query used:", query)
            return False

    def _escape_string(self, fieldname, value, sd=None, singleqoute_to_double=False):
        if singleqoute_to_double:
            value = value.replace("'", "''")
        if not fieldname or sd.field[fieldname].dataType in SQL.escape_string:
            return "'" + value + "'"
        else:
            return value

    def get_observations(self, uuid, start=None, end=None, format='json', onlyLast=False, fields=None):
        from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement

        w = self.rm.getWrapperByUUID(uuid)
        if not w:
            return None

        sd = w.getSensorDescription()

        # prepare query
        _filter = ["sensor_uuid = '%s'" % uuid]
        order = " ORDER BY sampling_time"
        if onlyLast:
            order += " DESC LIMIT 1"
        else:
            if start:
                _filter.append("sampling_time >= TIMESTAMP '%s'" % start)
            if end:
                _filter.append("sampling_time <= TIMESTAMP '%s'" % end)
        _filter = "WHERE " + " and ".join(_filter)

        if fields:
            fields = fields.split(',')
            fields_ = []
            for ft in fields:
                fields_.append("data->'%s' AS %s" % (ft, ft))
            fields_.append("quality")
        else:
            fields_ = SQL.cp_observation_fields

        query = "SELECT %s FROM %s.cp_observations %s %s;" % (",".join(fields_), SQL.SCHEMA, _filter, order)
        L.d("SQL: executing query", query)

        try:
            # need a new cursor object to no interfere with the state of the class's inserting cursor
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            data2 = [list(x) for x in data]
            del data
            if format in ('n3', 'nt', 'xml', 'turtle', 'pretty-xml', 'trix'):
                if ResourceManagement.args.messagebus or ResourceManagement.args.triplestore:
                    if fields:
                        observations = []
                        qualities = []
                        for x in data2:
                            tmp = JOb()
                            for i in range(0, len(fields)):
                                ft = fields[i]
                                tmp[ft] = JOb(x[i])
                            tmp.fields = fields
                            observations.append(tmp)
                            qualities.append(JOb(x[-1]))
                    else:
                        observations = [JOb(x[3]) for x in data2]
                        qualities = [JOb(x[4]) for x in data2]
                    g = self.rm.annotator.annotateObservation(observations, sd, None, qualities)
                    del observations
                    del qualities
                    del query
                    return g.serialize(format=format)
                else:
                    return "Error: requires messagebus or triplestore to be enabled"
            else:
                # search in all columns in each row for a datetime.datetime and parse it
                for i in range(0, len(data2)):
                    data2[i] = map(lambda x: x.strftime("%Y-%m-%d %H:%M:%S") if isinstance(x, datetime.datetime) else x, data2[i])
                json_list = []
                for x in data2:
                    if fields:
                        y = JOb({})
                        for i in range(0, len(fields)):
                            ft = fields[i]
                            y[ft] = JOb(x[i])
                        y.quality = JOb(x[-1])
                        y.fields = fields
                    else:
                        y = JOb(x[3])
                        y.quality = JOb(x[4])
                    json_list.append(y)
                del query
                return JOb(json_list).dumps()

        except Exception as e:
            L.e("SQL:", e)
            L.e("SQL query used:", query)
            return "Error: " + str(e)

    def data_timeframe(self, uuid):
        """
        return the minimum and maximum sampling_time as tuple (min, max) for a sensor identified by the parameter uuid.
        If no sensor with the uuid is found in the database (None, None) is returned.
        :param uuid:
        :return:
        """
        query = "SELECT min(sampling_time), max(sampling_time) FROM %s.cp_observations WHERE sensor_uuid = '%s';" % (SQL.SCHEMA, uuid)
        # need a new cursor object to no interfere with the state of the class's inserting cursor
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 1:
            d1, d2 = data[0]
            return d1.strftime("%Y-%m-%dT%H:%M:%S%z"), d2.strftime("%Y-%m-%dT%H:%M:%S%z")

        else:
            return None, None

    def get_observations_service_category(self, service_category, start=None, end=None):
        cursor = self.conn.cursor()
        query = "SELECT sensor_uuid from cp_sensors WHERE sercvice_category = '" + service_category + "';"
        cursor.execute(query)
        data = cursor.fetchall()
        for sensor_uuid, in data:
            yield self.get_observations(sensor_uuid, start, end, format='nt')
        return

# if __name__ == "__main__":
#     cnf = JOb({
#     "host": "localhost",
#     "port": 5438,
#     "username": "wp4",
#     "password": "wp4natss!",
#     "database": "cp_sweden"
#   })
#     sql = SQL(cnf, None)
#     print "ok"
