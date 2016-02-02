'''
Created on Aug 4, 2015

@author: danielk,uaso
'''
from shapely.geometry import Point
from shapely.wkt import loads
import psycopg2
from virtualisation.misc.log import Log as L

class CityPulseGDInterface(object):
    '''
    classdocs
    '''

    def __init__(self, gdi_config):
        connect_str = "host='%s' dbname='%s' user='%s' password='%s' port=%d" % (
        gdi_config.host, gdi_config.database, gdi_config.username, gdi_config.password, gdi_config.port)
        self.conn = psycopg2.connect(connect_str)
        self.curs = self.conn.cursor()

    def registerSensorStreamFromPointLonLat(self, sensor_uuid, sensor_id, sercvice_category, lon, lat):
        geom = Point(lon, lat)
        return self.__registerSensorStream(sensor_uuid, sensor_id, sercvice_category, geom, 4326)

    def registerSensorStreamFromPoint(self, sensor_uuid, sensor_id, sercvice_category, x, y, epsg):
        geom = Point(x, y)
        return self.__registerSensorStream(sensor_uuid, sensor_id, sercvice_category, geom, epsg)

    def registerSensorStreamFromWKT(self, sensor_uuid, sensor_id, sercvice_category, wkt, epsg):
        geom = loads(wkt)
        return self.__registerSensorStream(sensor_uuid, sensor_id, sercvice_category, geom, epsg)

    def __registerSensorStream(self, sensor_uuid, sensor_id, sercvice_category, geom, epsg):
        sql = (
        "INSERT INTO cp_sensors(sensor_uuid, sensor_annotation_id, sercvice_category, geom) VALUES('%(sensor_uuid)s' , '%(sensor_id)s' , '%(sercvice_category)s' ,ST_Transform(st_setsrid('%(geom)s'::geometry,%(epsg)s),4326))" %
        {'sensor_uuid': sensor_uuid, 'sensor_id': sensor_id, 'sercvice_category': sercvice_category,
         'geom': geom.wkb_hex, 'epsg': epsg})
        try:
            self.curs.execute(sql)
            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            L.e("Cannot insert Sensor:", str(
                {'sensor_uuid': sensor_uuid, 'sensor_id': sensor_id, 'sercvice_category': sercvice_category,
                 'geom': geom.wkb_hex, 'epsg': epsg}))
            L.e("SQL query used:", sql)
            return False

    def getSensorStream(self, sensor_uuid):
        self.curs.execute("SELECT *, ST_AsText(geom) FROM cp_sensors where sensor_uuid='" + sensor_uuid + "'")
        return (self.curs.fetchone())

    def removeSensorStream(self, sensor_uuid):
        sql = ("DELETE FROM cp_sensors WHERE sensor_uuid='%(sensor_uuid)s'" % {'sensor_uuid': sensor_uuid})
        try:
            self.curs.execute(sql)
            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            L.e("Cannot delete Sensor: " + str({'sensor_uuid': sensor_uuid}))
            L.e("SQL query used:", sql)
            return False

    def removeAllSensorStreams(self):
        try:
            sql = "DELETE FROM cp_sensors"
            self.curs.execute(sql)
            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            L.e("Cannot delete all Sensors")
            L.e("SQL query used", sql)
            return False
