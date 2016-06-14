
__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.log import Log
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.history.csvhistory import CSVHistoryReader
from virtualisation.wrapper.parser.csvparser import CSVParser
from virtualisation.wrapper.parser.jsonparser import JSONParser

from virtualisation.wrapper.connection.httpconnection import HttpPullConnection
from virtualisation.wrapper.splitter.abstractsplitter import AbstractSplitter
import urlparse

import os.path
import uuid

class AarhusTrafficConnection(HttpPullConnection):
    def __init__(self, wrapper):
        super(AarhusTrafficConnection, self).__init__(wrapper)

    def next(self):
        attempts = 0
        maxattempts = 10 # in a normal case 3 attempts should be sufficient, meaning about 3 attempts per page
        url = self.wrapper.getSensorDescription()[0].source
        urlsplited = urlparse.urlsplit(url)
        urlbase = urlsplited.scheme + "://" + urlsplited.netloc
        s = self.load(url)
        # print url, s
        if s:
            x = JOb(s)
            result = x.result
            total = result.total
            while total > len(result.records) and attempts < maxattempts:
                attempts += 1
                print "attempts", attempts
                url = urlbase + x.result._links.next
                s = self.load(url)
                if s:
                    x = JOb(s)
                    result["records"] += x.result["records"]
                else:
                    break
            # print result
            return result
        return None

class AarhusTrafficSplitter(AbstractSplitter):
    def __init__(self, wrapper):
        super(AarhusTrafficSplitter, self).__init__(wrapper)
        self.data = None

    def next(self, sensorDescription):
        if not self.data:
            return None
        else:
            return self.data[sensorDescription.sensorID] if sensorDescription.sensorID in self.data else None

    def update(self, data):
        if data:
            self.data = {}
            for record in data.records:
                self.data[record.REPORT_ID] = record
        else:
            self.data = None

class InternalWrapper(AbstractWrapper):

    def __init__(self, sensorDescription):
        super(InternalWrapper, self).__init__()
        self.sensorDescription = sensorDescription
        self.parser = JSONParser(self)

    def getSensorDescription(self):
        return self.sensorDescription
    
    def setReplayMode(self, mode):
        if mode:
            try:
                Log.i("loading history for", self.sensorDescription.sensorID, "...")
                self.historyreader = CSVHistoryReader(self, AbstractWrapper.getFileObject(__file__, os.path.join("historicdata", "trafficData%d.csv" % self.sensorDescription.sensorID), "rU"))
                self.historyreader.multiple_observations = False
                Log.i("done")
                self.historyparser = CSVParser(self, self.historyreader.headers)
                # connection will be set automatically by the AbstractComposedWrapper to SplitterConnection
            except Exception as e:
                Log.e(e)
                self.historyreader = None
        super(InternalWrapper, self).setReplayMode(mode)

class AarhusTrafficWrapper(AbstractComposedWrapper):

    def __init__(self):
        super(AarhusTrafficWrapper, self).__init__()
        metadatafile = AbstractComposedWrapper.getFileObject(__file__, "aarhus-traffic-points.json", "rU")
        metadata = JOb(metadatafile)

        basesensordescription = SensorDescription()
        basesensordescription.source = "http://www.odaa.dk/api/action/datastore_search?resource_id=b3eeb0ff-c8a8-4824-99d6-e0a3747c8b0d"
        basesensordescription.namespace = "http://ict-citypulse.eu/"
        basesensordescription.author = "cityofaarhus" #or id of user profile
        basesensordescription.sensorType = "Aarhus_Road_Traffic" #serviceCategory
        basesensordescription.graphName = "aarhus_road_traffic#"
        basesensordescription.sourceType = "pull_http"
        basesensordescription.sourceFormat = "application/json" #MIMEs
        basesensordescription.information = "Road traffic for the City of Aarhus"
        # basesensordescription.cityName = "Aarhus"
        # basesensordescription.countryName = "Denmark"
        basesensordescription.movementBuffer = 3 # in meter, 0 means stationary
        basesensordescription.maxLatency = 2
        basesensordescription.updateInterval = 60 * 5  # with push an interval to send a keep alive message
        basesensordescription.fields = "TIMESTAMP, avgSpeed, vehicleCount, avgMeasuredTime".split(", ")

        basesensordescription.field.avgSpeed.propertyName = "AverageSpeed"
        basesensordescription.field.avgSpeed.propertyURI = basesensordescription.namespace + "city#AverageSpeed"
        basesensordescription.field.avgSpeed.unit = basesensordescription.namespace + "unit:km-per-hour"
        basesensordescription.field.avgSpeed.min = 0
        basesensordescription.field.avgSpeed.max = 250
        basesensordescription.field.avgSpeed.dataType = "float"
        basesensordescription.field.avgSpeed.showOnCityDashboard = True
        basesensordescription.field.avgSpeed.aggregationMethod = "sax"
        basesensordescription.field.avgSpeed.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 4}


        basesensordescription.field.vehicleCount.propertyName = "StreetVehicleCount"
        basesensordescription.field.vehicleCount.propertyURI = basesensordescription.namespace + "city#StreetVehicleCount"
        basesensordescription.field.vehicleCount.unit = basesensordescription.namespace + "unit:number-of-vehicle-per-5min"
        basesensordescription.field.vehicleCount.min = 0
        basesensordescription.field.vehicleCount.max = 1000
        basesensordescription.field.vehicleCount.dataType = "int"
        basesensordescription.field.vehicleCount.showOnCityDashboard = True
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 4}


        basesensordescription.field.avgMeasuredTime.propertyName = "MeasuredTime"
        # basesensordescription.field.avgMeasuredTime.propertyName = "Property"
        # basesensordescription.field.avgMeasuredTime.propertyPrefix = "ssn"
        basesensordescription.field.avgMeasuredTime.propertyURI = basesensordescription.namespace + "city#AvgMeasuredTime"
        basesensordescription.field.avgMeasuredTime.unit = "http://purl.oclc.org/NET/muo/ucum/unit/time/minute" # basesensordescription.namespace + "unit:minutes"
        basesensordescription.field.avgMeasuredTime.min = 0
        basesensordescription.field.avgMeasuredTime.max = 1000
        basesensordescription.field.avgMeasuredTime.dataType = "int"

        basesensordescription.field.TIMESTAMP.propertyName = "MeasuredTime"
        basesensordescription.field.TIMESTAMP.propertyURI = basesensordescription.namespace + "city#MeasuredTime"
        basesensordescription.field.TIMESTAMP.unit = "http://purl.oclc.org/NET/muo/ucum/unit/time/minute" # basesensordescription.namespace + "unit:time#minutes"
        basesensordescription.field.TIMESTAMP.min = "2012-01-01T00:00:00"
        basesensordescription.field.TIMESTAMP.max = "2099-12-31T23:59:59"
        basesensordescription.field.TIMESTAMP.dataType = "datetime.datetime"
        basesensordescription.field.TIMESTAMP.format = "%Y-%m-%dT%H:%M:%S"
        basesensordescription.field.TIMESTAMP.skip_annotation = True

        basesensordescription.timestamp.inField = "TIMESTAMP"
        basesensordescription.timestamp.format = "%Y-%m-%dT%H:%M:%S"

        for point in metadata.result.records:
            sensordescription = basesensordescription.deepcopy()
            sensordescription.sensorName = "aarhus_road_traffic_" + str(point.REPORT_ID)
            sensordescription.sensorID = point.REPORT_ID
            sensordescription.fullSensorID = basesensordescription.namespace + "sensor/" + str(point.REPORT_ID)
            sensordescription.location = "LINESTRING(%s %s, %s %s)" % (point.POINT_1_LNG, point.POINT_1_LAT, point.POINT_2_LNG, point.POINT_2_LAT)
            sensordescription.cityName = [self.__getattr(point, "POINT_1_CITY", "n/a"), self.__getattr(point, "POINT_1_CITY", "n/a")]
            sensordescription.countryName = [self.__getattr(point, "POINT_1_COUNTRY", "n/a"), self.__getattr(point, "POINT_2_COUNTRY", "n/a")]
            sensordescription.streetName = [self.__getattr(point, "POINT_1_STREET", "n/a"), self.__getattr(point, "POINT_2_STREET", "n/a")]
            sensordescription.postalCode = [self.__getattr(point, "POINT_1_POSTAL_CODE", "n/a"), self.__getattr(point, "POINT_2_POSTAL_CODE", "n/a")]
            sensordescription.messagebus.routingKey = "Aarhus.Road.Traffic." + str(point.REPORT_ID)
            self.addWrapper(InternalWrapper(sensordescription))

        self.splitter = AarhusTrafficSplitter(self)
        self.connection = AarhusTrafficConnection(self)

    def __getattr(self, o, n, d):
        """
        like getattr with default d, if object o does not contain attribute n
        :param o:
        :param n:
        :param d:
        :return:
        """
        if n in o and getattr(o, n) is not None:
            return getattr(o, n)
        else:
            return d
