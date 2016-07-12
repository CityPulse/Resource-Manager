# coding=utf-8
__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.history.csvhistory import CSVHistoryReader
from virtualisation.wrapper.parser.csvparser import CSVParser
from virtualisation.wrapper.parser.jsonparser import JSONParser
from virtualisation.wrapper.connection.httpconnection import HttpPullConnection
from virtualisation.misc.log import Log
import os.path

class BrasovPollutionConnection(HttpPullConnection):
    def __init__(self, wrapper):
        super(BrasovPollutionConnection, self).__init__(wrapper)

    def next(self):
        data = super(BrasovPollutionConnection, self).next()
        if not data or data.strip() == "Measurement not available":
            return None
        else:
            return data

class InternalBrasovWrapper(AbstractWrapper):

    def __init__(self, sensorDescription):
        super(InternalBrasovWrapper, self).__init__()
        self.sensorDescription = sensorDescription
        self.connection = BrasovPollutionConnection(self)
        self.parser = JSONParser(self)

    def getSensorDescription(self):
        return self.sensorDescription

    def setReplayMode(self, mode):
        if mode:
            try:
                self.historyreader = CSVHistoryReader(self, AbstractWrapper.getFileObject(__file__, os.path.join("historicdata", "pollution-%s.csv" % self.sensorDescription.sensorID), "rU"), delimiter=';')
                self.historyparser = CSVParser(self, self.historyreader.headers)
            except Exception as e:
                Log.e(e)
                self.historyreader = None
        super(InternalBrasovWrapper, self).setReplayMode(mode)

class BrasovPollutionWrapper(AbstractComposedWrapper):

    def __init__(self):
        super(BrasovPollutionWrapper, self).__init__()

        basesensordescription = SensorDescription()
        basesensordescription.namespace = "http://ict-citypulse.eu/"
        basesensordescription.author = "cityofbrasov"
        basesensordescription.graphName = "brasov_air_pollution#"
        basesensordescription.sourceType = "pull_http"
        basesensordescription.sourceFormat = "application/json"
        basesensordescription.information = "Air pollution in the city of Brasov"
        basesensordescription.cityName = "Brasov"
        basesensordescription.countryName = "Romania"
        basesensordescription.movementBuffer = 0
        basesensordescription.maxLatency = 2
        basesensordescription.updateInterval = 60 * 5
        basesensordescription.fields = ['aqisitionStation', 'aqisitionStationDetails', 'eventTypeName', 'qualityLevelType', 'timestamp']

        basesensordescription.field.aqisitionStation.propertyName = "Property"
        basesensordescription.field.aqisitionStation.propertyPrefix = "ssn"
        basesensordescription.field.aqisitionStation.propertyURI = basesensordescription.namespace + "brasov/pollution#Station"
        basesensordescription.field.aqisitionStation.min = ""
        basesensordescription.field.aqisitionStation.max = ""
        basesensordescription.field.aqisitionStation.dataType = "str"
        basesensordescription.field.aqisitionStation.showOnCityDashboard = True

        basesensordescription.field.aqisitionStationDetails.propertyName = "Property"
        basesensordescription.field.aqisitionStationDetails.propertyPrefix = "ssn"
        basesensordescription.field.aqisitionStationDetails.propertyURI = basesensordescription.namespace + "brasov/pollution#StationDetails"
        basesensordescription.field.aqisitionStationDetails.min = ""
        basesensordescription.field.aqisitionStationDetails.max = ""
        basesensordescription.field.aqisitionStationDetails.dataType = "str"
        basesensordescription.field.aqisitionStationDetails.showOnCityDashboard = True

        basesensordescription.field.eventTypeName.propertyName = "AirPollutionIndex"
        basesensordescription.field.eventTypeName.propertyURI = basesensordescription.namespace + "brasov/pollution#EventType"
        basesensordescription.field.eventTypeName.min = ""
        basesensordescription.field.eventTypeName.max = ""
        basesensordescription.field.eventTypeName.dataType = "str"
        basesensordescription.field.eventTypeName.showOnCityDashboard = True

        basesensordescription.field.qualityLevelType.propertyName = "AirPollutionLevel"
        basesensordescription.field.qualityLevelType.propertyURI = basesensordescription.namespace + "brasov/pollution#QualityLevelType"
        basesensordescription.field.qualityLevelType.min = ""
        basesensordescription.field.qualityLevelType.max = ""
        basesensordescription.field.qualityLevelType.dataType = "str"
        basesensordescription.field.qualityLevelType.showOnCityDashboard = True

        basesensordescription.field.timestamp.propertyName = "MeasuredTime"
        basesensordescription.field.timestamp.propertyURI = basesensordescription.namespace + "city#MeasuredTime"
        basesensordescription.field.timestamp.unit = basesensordescription.namespace + "unit:time"
        basesensordescription.field.timestamp.min = ""
        basesensordescription.field.timestamp.max = ""
        basesensordescription.field.timestamp.dataType = "str"        
        basesensordescription.field.timestamp.skip_annotation = True

        basesensordescription.timestamp.inField = "timestamp"
        basesensordescription.timestamp.format = "UNIX5"

        locations = [
            ("BV-1", "Brasov, Calea Bucuresti, Str. Soarelui", "POINT(25.63272 45.636742)"),
            ("BV-2", "Brasov, Str. Castanilor, FN, cod postal 500097", "POINT(25.604125 45.649339)"),
            ("BV-3", "Brasov, Bdul. Garii, Aleea Lacramioarelor", "POINT(25.6169 45.658564)"),
            ("BV-4", "Brasov, Sanpetru, Str. Morii, FN", "POINT(25.625372 45.718173)"),
            ("BV-5", "Brasov, Bdul. Vlahuta, Str. Parcul Mic, Nr. 9", "POINT(25.625952 45.651784)")
        ]

        eventTypeNames = ["SO2", "PM10", "NO2", "O3", "CO"]

        for _id, loc, coords in locations:
            for eventTypeName in eventTypeNames:
                sensordescription = basesensordescription.deepcopy()
                sensordescription.source = "http://www.bamct.siemens.ro:9000/brasovDataCollector/pollutionView?location=%s&pollutionType=%s" % (_id, eventTypeName)
                sensordescription.sensorName = "brasov_air_pollution_%s_%s" % (eventTypeName, _id)
                sensordescription.sensorID = _id + "-" + eventTypeName
                sensordescription.fullSensorID = basesensordescription.namespace + "brasov/pollution/" + _id + "/" + eventTypeName
                sensordescription.location = coords
                #sensordescription.sensorType = "Brasov_Air_Pollution_" + eventTypeName
                sensordescription.sensorType = "Brasov_Air_Pollution"

                sensordescription.field.aqisitionStation.equals = _id
                sensordescription.field.aqisitionStationDetails.equals = loc
                sensordescription.field.eventTypeName.equals = eventTypeName

                sensordescription.messagebus.routingKey = "Brasov.Air.Pollution.%s.%s" % (eventTypeName, _id)

                self.addWrapper(InternalBrasovWrapper(sensordescription))
