
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

import os.path
import uuid
import csv
import xml.etree.ElementTree as ET

def nicename(x):
    return x.replace(" ", "_").replace("+", "_")

class AarhusParkingSplitterJson(AbstractSplitter):
    def __init__(self, wrapper):
        super(AarhusParkingSplitterJson, self).__init__(wrapper)
        self.data = None

    def next(self, sensorDescription):
        if not self.data:
            return None
        else:
            return self.data[sensorDescription.sensorID]

    def update(self, data):
        if data:
            self.data = {}
            tmp = JOb(data)
            for r in tmp.result.records:
                _gc = nicename(r.garageCode)
                _r = r.raw()
                self.data[_gc] = {}
                for x in r.raw():
                    self.data[_gc][x] = _r[x]
            print "data", self.data
        else:
            self.data = None

class InternalWrapper(AbstractWrapper):

    def __init__(self, sensorDescription):
        super(InternalWrapper, self).__init__()
        self.sensorDescription = sensorDescription
        self.parser = JSONParser(self)
        # self.connection = default splitter connection

    def getSensorDescription(self):
        return self.sensorDescription

    def setReplayMode(self, mode):
        if mode:
            try:
                Log.i("loading history data for", self.sensorDescription.sensorID, "...")
                self.historyreader = CSVHistoryReader(self, AbstractWrapper.getFileObject(__file__, os.path.join("historicdata", "aarhus_parking-%s.csv" % self.sensorDescription.sensorID), "rU"), timestampfield="updatetime")
                # Must preserve the order as in the CSV but use the names as in senordescription.fields
                # vehiclecount,updatetime,_id,totalspaces,garagecode,streamtime
                self.historyparser = CSVParser(self, ["vehicleCount", "updatetime", "_id", "totalSpaces", "garageCode", "st"], timestampfield="updatetime")
                Log.i("done")

            except Exception as e:
                Log.e(e)
                self.historyreader = None
        super(InternalWrapper, self).setReplayMode(mode)


class AarhusParkingWrapper(AbstractComposedWrapper):

    def __init__(self):
        super(AarhusParkingWrapper, self).__init__()
        metadatafile = AbstractComposedWrapper.getFileObject(__file__, "aarhus_parking-address.csv", "rU")

        basesensordescription = SensorDescription()
        basesensordescription.source = "http://www.odaa.dk/api/action/datastore_search?resource_id=2a82a145-0195-4081-a13c-b0e587e9b89c"
        basesensordescription.namespace = "http://ict-citypulse.eu/"
        basesensordescription.author = "cityofaarhus"
        basesensordescription.sensorType = "Aarhus_Road_Parking"
        basesensordescription.graphName = "aarhus_road_parking#"
        basesensordescription.sourceType = "pull_http"
        basesensordescription.sourceFormat = "application/xml"
        basesensordescription.information = "Parking data for the City of Aarhus"
        basesensordescription.cityName = "Aarhus"
        basesensordescription.countryName = "Denmark"
        basesensordescription.movementBuffer = 3
        basesensordescription.maxLatency = 2
        basesensordescription.updateInterval = 60
        # basesensordescription.fields = ["vehicleCount", "totalSpaces", "garageCode"]
        basesensordescription.fields = ["vehicleCount", "totalSpaces"]

        # basesensordescription.field.garageCode.propertyName = "Property"
        # basesensordescription.field.garageCode.propertyPrefix = "ssn"
        # basesensordescription.field.garageCode.propertyURI = basesensordescription.namespace + "city#Garagecode"
        # basesensordescription.field.garageCode.min = ""
        # basesensordescription.field.garageCode.max = ""
        # basesensordescription.field.garageCode.dataType = "str"

        basesensordescription.field.totalSpaces.propertyName = "ParkingCapacity"
        basesensordescription.field.totalSpaces.propertyURI = basesensordescription.namespace + "city#TotalSpaces"
        # basesensordescription.field.totalSpaces.unit = "http://muo.net/Number"
        basesensordescription.field.totalSpaces.min = 0
        basesensordescription.field.totalSpaces.max = 10000
        basesensordescription.field.totalSpaces.dataType = "int"
        basesensordescription.field.totalSpaces.showOnCityDashboard = True
        basesensordescription.field.totalSpaces.aggregationMethod = None

        basesensordescription.field.vehicleCount.propertyName = "ParkingVehicleCount"
        basesensordescription.field.vehicleCount.propertyURI = basesensordescription.namespace + "city#ParkingVehicleCount"
        basesensordescription.field.vehicleCount.unit = basesensordescription.namespace + "unit:number-of-vehicle-per-1min"
        basesensordescription.field.vehicleCount.min = 0
        basesensordescription.field.vehicleCount.max = "@totalSpaces"
        basesensordescription.field.vehicleCount.dataType = "int"
        basesensordescription.field.vehicleCount.showOnCityDashboard = True
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}

        # basesensordescription.timestamp.inField = "updatetime"
        basesensordescription.timestamp.format = "%Y-%m-%d %H:%M:%S"

        metadata = csv.DictReader(metadatafile)

        for row in metadata:
            sensordescription = basesensordescription.deepcopy()
            sensordescription.sensorName = "aarhus_road_parking_" + nicename(row['garagecode'])
            sensordescription.sensorID = nicename(row['garagecode'])
            sensordescription.fullSensorID = basesensordescription.namespace + "sensor/" + sensordescription.sensorID
            sensordescription.location = "POINT(%s %s)" % (row['longitude'], row['latitude'])
            sensordescription.messagebus.routingKey = "Aarhus.Road.Parking." + sensordescription.sensorID
            sensordescription.streetName = self.__getattr(row, "street", "n/a")
            sensordescription.postalCode = self.__getattr(row, "postalcode", "n/a")

            # garage code only as sensorID embedded in an URI. Possibilities to read it unknown at this point.
            # sensordescription.staticproperties.garageCode.propertyName = "Property"
            # sensordescription.staticproperties.garageCode.propertyPrefix = "ssn"
            # sensordescription.staticproperties.garageCode.propertyURI = basesensordescription.namespace + "city#Garagecode"
            # sensordescription.staticproperties.garageCode.dataType = "str"
            # sensordescription.staticproperties.garageCode.value = sensordescription.sensorID

            self.addWrapper(InternalWrapper(sensordescription))

        self.connection = HttpPullConnection(self, basesensordescription.source)
        self.splitter = AarhusParkingSplitterJson(self)
        # self.update()

    def __getattr(self, o, n, d):
        """
        like getattr with default d, if object o does not contain attribute n
        :param o:
        :param n:
        :param d:
        :return:
        """
        if n in o and o[n] is not None:
            return o[n]
        else:
            return d