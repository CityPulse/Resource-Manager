
__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


from virtualisation.wrapper.abstractwrapper import AbstractWrapper
from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.parser.jsonparser import JSONParser
from virtualisation.wrapper.connection.httpconnection import HttpPullConnection
import threading
from TwitterAPI import TwitterAPI, TwitterOAuth
import mysql.connector
from mysql.connector import errorcode
import mysql.connector.locales.eng

#location = '10.050253,56.098242,10.288175,56.213350' # Aarhus
#location = '7.938317,52.264523,8.152550,52.425601' # Osna
#location = '-122.75,36.8,-121.75,37.8' # SF
#location = '-74,40,-73,41' # NY
#location = '13.254,52.403,13.679,52.683' # Berlin
#location = '-74,40,-73,41' # NY

class MysqlConfig(object):

    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    @classmethod
    def read_file_object(cls, fileobject):
        v = {}
        for line in fileobject:
            if '=' in line:
                name, value = line.split('=', 1)
                v[name.strip()] = value.strip()
        return MysqlConfig(
            v['username'],
            v['password'],
            v['host'],
            v['database'])

class TwitterConnection(HttpPullConnection):
    def __init__(self, wrapper, location):
        super(TwitterConnection, self).__init__(wrapper)
        self.location = location
        self.tweet = None
        self.abort = threading.Event()

    def next(self):
        return self.tweet

    def run_async(self):
        auth = TwitterOAuth.read_file_object(self.wrapper.getFileObject(__file__, "TwitterAPI/credentials.txt"))
        api = TwitterAPI(auth.consumer_key, auth.consumer_secret, auth.access_token_key, auth.access_token_secret)
        try:
            r = api.request('statuses/filter', {'locations': self.location})
            #r = api.request('statuses/filter', {'track':'pizza'})
        except:
            print r.text

        for item in r:
            self.tweet = item
            self.wrapper.update()
            if self.abort.is_set():
                break


class TwitterParser(JSONParser):
    def __init__(self, wrapper, tablename):
        super(TwitterParser, self).__init__(wrapper)

        mysql_config = MysqlConfig.read_file_object(wrapper.getFileObject(__file__, "mysql.txt"))

        # connection to MySQL DB
        try:
            self.db = mysql.connector.connection.MySQLConnection(user=mysql_config.username,
                                                                 password=mysql_config.password,
                                                                 host=mysql_config.host,
                                                                 database=mysql_config.database)
            self.cur = self.db.cursor()

            # create the table if not exists
            self.cur.execute("""CREATE TABLE IF NOT EXISTS `%s` (
  `twitterid` varchar(100) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `text` varchar(1000) NOT NULL,
  `time` varchar(100) NOT NULL,
  `lat` varchar(100) NOT NULL,
  `long` varchar(100) NOT NULL,
  `boundingbox` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;""" % tablename)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print err

        self.tablename = tablename
        self.insert_stmt = "INSERT INTO " + self.tablename + " (twitterid, userid, text, time, lat, `long`, boundingbox) VALUES (%(tweet_id)s, %(user_id)s, %(text)s, %(timestamp)s, %(lat)s, %(long)s, %(bounding_box)s)"

    def parse(self, data, clock):
        if not data:  # nothing received or nothing in the history -> nothing to parse
            return None

        data = JOb(data)
        result = JOb()
        result.text = data.text
        result.user_id = data.user.id
        result.timestamp = data.timestamp_ms
        result.tweet_id = data.id
        result.bounding_box = "[" + ";".join([",".join(map(str, a)) for a in data.place.bounding_box.coordinates[0]]) + "]"

        result.lat = ""
        result.long = ""
        if 'coordinates' in data and data.coordinates is not None and data.coordinates.type == "Point":
            result.long = str(data.coordinates.coordinates[0])
            result.lat  = str(data.coordinates.coordinates[1])

        # insert into DB
        if hasattr(self, 'cur'):
            self.cur.execute(self.insert_stmt, result.raw())
            self.db.commit()

        result.geotag = self.geometry_to_wkt(data.geo) if data.geo else ""
        # print result

        del data
        return super(TwitterParser, self).parse(result, clock)

    def geometry_to_wkt(self, geometry):
        return "".join([geometry.type.upper(), "(", " ".join(map(str, geometry.coordinates)), ")"]) if geometry.type == "Point" else \
             "".join([geometry.type.upper(), "(", ', '.join([' '.join([str(x), str(y)]) for x, y in geometry.coordinates[0]]), ")"])


class LocationBasedTwitterWrapper(AbstractWrapper):

    def __init__(self, cityname, cityshort, coordinates, tablename, country=None):
        super(LocationBasedTwitterWrapper, self).__init__()
        self.thread = None

        self.sensorDescription = SensorDescription()
        self.sensorDescription.source = "http://www.twitter.com"
        self.sensorDescription.namespace = "http://ict-citypulse.eu/"
        self.sensorDescription.author = "twitter"
        self.sensorDescription.sensorType = "Twitter_" + cityname #serviceCategory
        self.sensorDescription.graphName = "twitter_%s#" % cityname.lower()
        self.sensorDescription.sourceType = "push_http"
        self.sensorDescription.sourceFormat = "application/json" #MIMEs
        self.sensorDescription.information = "Twitter stream of " + cityname
        self.sensorDescription.cityName = cityname
        if country:
            self.sensorDescription.countryName = country
        self.sensorDescription.movementBuffer = 3
        self.sensorDescription.maxLatency = 2
        self.sensorDescription.updateInterval = 60 * 5
        self.sensorDescription.fields = ["text", "user_id", "timestamp", "tweet_id", "geotag", "bounding_box"]

        self.sensorDescription.sensorName = "Twitter_" + cityshort
        self.sensorDescription.sensorID = "T" + cityshort
        self.sensorDescription.fullSensorID = self.sensorDescription.namespace + "sensor/" + self.sensorDescription.sensorID
        self.sensorDescription.location = self.coordinates_to_polygon(coordinates, geometry_name='LINESTRING')
        self.sensorDescription.messagebus.routingKey = "Twitter." + cityshort
        self.sensorDescription.no_publish_messagebus = True

        # self.sensorDescription.field.vehicleCount.showOnCityDashboard = True
        # self.sensorDescription.field.vehicleCount.aggregationMethod = "sax"
        # self.sensorDescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
        #                                                                 "unit_of_window": "hours", "window_duration": 4}

        self.sensorDescription.field.text.propertyName = "Property"
        self.sensorDescription.field.text.propertyPrefix = "ssn"
        self.sensorDescription.field.text.propertyURI = self.sensorDescription.namespace + "city#Tweet"
        self.sensorDescription.field.text.dataType = "str"
        # self.sensorDescription.field.text.skip_annotation = True

        self.sensorDescription.field.user_id.propertyName = "Property"
        self.sensorDescription.field.user_id.propertyPrefix = "ssn"
        self.sensorDescription.field.user_id.propertyURI = self.sensorDescription.namespace + "city#UserID"
        self.sensorDescription.field.user_id.dataType = "str"

        self.sensorDescription.field.tweet_id.propertyName = "Property"
        self.sensorDescription.field.tweet_id.propertyPrefix = "ssn"
        self.sensorDescription.field.tweet_id.propertyURI = self.sensorDescription.namespace + "city#TweetID"
        self.sensorDescription.field.tweet_id.dataType = "str"

        self.sensorDescription.field.geotag.propertyName = "Property"
        self.sensorDescription.field.geotag.propertyPrefix = "ssn"
        self.sensorDescription.field.geotag.propertyURI = self.sensorDescription.namespace + "city#Geo"
        self.sensorDescription.field.geotag.dataType = "str"

        self.sensorDescription.field.bounding_box.propertyName = "Property"
        self.sensorDescription.field.bounding_box.propertyPrefix = "ssn"
        self.sensorDescription.field.bounding_box.propertyURI = self.sensorDescription.namespace + "city#Location"
        self.sensorDescription.field.bounding_box.dataType = "str"

        self.sensorDescription.field.timestamp.propertyName = "MeasuredTime"
        self.sensorDescription.field.timestamp.propertyURI = self.sensorDescription.namespace + "city#MeasuredTime"
        self.sensorDescription.field.timestamp.unit = "http://purl.oclc.org/NET/muo/ucum/unit/time/minute" # self.sensorDescription.namespace + "unit:time#minutes"
        self.sensorDescription.field.timestamp.min = "2012-01-01T00:00:00"
        self.sensorDescription.field.timestamp.max = "2099-12-31T23:59:59"
        self.sensorDescription.field.timestamp.dataType = "datetime.datetime"
        self.sensorDescription.field.timestamp.format = "UNIX5"

        self.sensorDescription.timestamp.inField = "timestamp"
        self.sensorDescription.timestamp.format = "UNIX5"
        
        self.connection = TwitterConnection(self, ",".join(map(str, coordinates)))
        self.parser = TwitterParser(self, tablename)

    def getSensorDescription(self):
        return self.sensorDescription

    def run(self):
        self.thread = threading.Thread(target=self.connection.run_async, name="Twitter")
        self.thread.start()

    def stop(self):
        if self.thread:
            self.connection.abort.set()
            self.thread.join()
            if hasattr(self.parser, "db"):
                self.parser.db.close()
            self.thread = None

    def coordinates_to_polygon(self, coordinates, geometry_name='POLYGON'):
        P = lambda a: ' '.join(map(str, a))
        open_parenthesis = "(" * (2 if geometry_name == 'POLYGON' else 1)
        close_parenthesis = ")" * (2 if geometry_name == 'POLYGON' else 1)
        x1, y1, x2, y2 = coordinates
        l_down = (x1, y1)
        l_up = (x1, y2)
        r_up = (x2, y2)
        r_down = (x2, y1)
        return geometry_name + open_parenthesis + ', '.join([P(l_down), P(l_up), P(r_up), P(r_down), P(l_down)]) + close_parenthesis

class AarhusTwitterWrapper(LocationBasedTwitterWrapper):

    def __init__(self):
        # super(AarhusTwitterWrapper, self).__init__("New_York", "NY", [-74, 40, -73, 41], "AarhusTweet")
        super(AarhusTwitterWrapper, self).__init__("Aarhus", "AA", [10.050253,56.098242,10.288175,56.213350], "AarhusTweet")
