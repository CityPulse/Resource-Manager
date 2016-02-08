from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.log import Log
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.history.csvhistory import CSVHistoryReader
from virtualisation.wrapper.parser.csvparser import CSVParser
from virtualisation.wrapper.connection.dummyconnection import DummyConnection
import os.path

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class AarhusPollutionWrapper(AbstractWrapper):
    def __init__(self, sensorDescription):
        super(AarhusPollutionWrapper, self).__init__()
        self.sensorDescription = sensorDescription
        self.connection = DummyConnection(self)

    def getSensorDescription(self):
        return self.sensorDescription

    def setReplayMode(self, mode):
        if mode:
            try:
                Log.i("loading history for", self.sensorDescription.sensorID, "...")
                self.historyreader = CSVHistoryReader(self, AbstractWrapper.getFileObject(__file__,
                                                                                          os.path.join("historicdata",
                                                                                                       "pollutionData%s.csv" % self.sensorDescription.sensorID),
                                                                                          "rU"))
                Log.i("done")
                self.historyparser = CSVParser(self, self.historyreader.headers)
                # connection will be set automatically by the AbstractComposedWrapper to SplitterConnection
            except Exception as e:
                Log.e(e)
                self.historyreader = None
        super(AarhusPollutionWrapper, self).setReplayMode(mode)


class ComposedAarhusPollutionWrapper(AbstractComposedWrapper):
    def __init__(self):
        super(ComposedAarhusPollutionWrapper, self).__init__()
        metadatafile = AbstractComposedWrapper.getFileObject(__file__, "metadata.json", "rU")
        metadata = JOb(metadatafile)

        basesensordescription = SensorDescription()
        basesensordescription.source = "???" # TODO
        basesensordescription.namespace = "http://ict-citypulse.eu/"
        basesensordescription.author = "cityofaarhus"
        basesensordescription.sensorType = "Aarhus_Pollution"
        basesensordescription.graphName = "aarhus_pollution#"
        basesensordescription.sourceType = "pull_http"
        basesensordescription.sourceFormat = "application/json"
        basesensordescription.information = "Pollution data for the City of Aarhus"
        basesensordescription.cityName = "Aarhus"
        basesensordescription.countryName = "Denmark"
        basesensordescription.movementBuffer = 3
        basesensordescription.maxLatency = 2
        basesensordescription.updateInterval = 5 * 60
        basesensordescription.fields = ["ozone", "particullate_matter", "carbon_monoxide", "sulfure_dioxide",
                                        "nitrogen_dioxide", "longitude", "latitude", "timestamp"]

        basesensordescription.field.ozone.propertyName = "Property"
        basesensordescription.field.ozone.propertyPrefix = "ssn"
        basesensordescription.field.ozone.propertyURI = basesensordescription.namespace + "city#Ozone"
        basesensordescription.field.ozone.unit = basesensordescription.namespace + "unit:km-per-hour"
        basesensordescription.field.ozone.min = 0
        basesensordescription.field.ozone.max = 150
        basesensordescription.field.ozone.dataType = "int"
        basesensordescription.field.ozone.showOnCityDashboard = True
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.particullate_matter.propertyName = "Property"
        basesensordescription.field.particullate_matter.propertyPrefix = "ssn"
        basesensordescription.field.particullate_matter.propertyURI = basesensordescription.namespace + "city#ParticleMatter"
        basesensordescription.field.particullate_matter.unit = basesensordescription.namespace + "unit:number-of-vehicle-per-5min"
        basesensordescription.field.particullate_matter.min = 0
        basesensordescription.field.particullate_matter.max = 10000
        basesensordescription.field.particullate_matter.dataType = "int"
        basesensordescription.field.particullate_matter.showOnCityDashboard = True
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.carbon_monoxide.propertyName = "Property"
        basesensordescription.field.carbon_monoxide.propertyPrefix = "ssn"
        basesensordescription.field.carbon_monoxide.propertyURI = basesensordescription.namespace + "city#CarbonMonoxide"
        basesensordescription.field.carbon_monoxide.unit = basesensordescription.namespace + "unit:minutes"
        basesensordescription.field.carbon_monoxide.min = 0
        basesensordescription.field.carbon_monoxide.max = 1000
        basesensordescription.field.carbon_monoxide.dataType = "int"
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.sulfure_dioxide.propertyName = "Property"
        basesensordescription.field.sulfure_dioxide.propertyPrefix = "ssn"
        basesensordescription.field.sulfure_dioxide.propertyURI = basesensordescription.namespace + "city#SulfureDioxide"
        basesensordescription.field.sulfure_dioxide.unit = basesensordescription.namespace + "unit:minutes"
        basesensordescription.field.sulfure_dioxide.min = 0
        basesensordescription.field.sulfure_dioxide.max = 1000
        basesensordescription.field.sulfure_dioxide.dataType = "int"
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.nitrogen_dioxide.propertyName = "Property"
        basesensordescription.field.nitrogen_dioxide.propertyPrefix = "ssn"
        basesensordescription.field.nitrogen_dioxide.propertyURI = basesensordescription.namespace + "city#NitrogenDioxide"
        basesensordescription.field.nitrogen_dioxide.unit = basesensordescription.namespace + "unit:minutes"
        basesensordescription.field.nitrogen_dioxide.min = 0
        basesensordescription.field.nitrogen_dioxide.max = 1000
        basesensordescription.field.nitrogen_dioxide.dataType = "int"
        basesensordescription.field.vehicleCount.aggregationMethod = "sax"
        basesensordescription.field.vehicleCount.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.longitude.propertyName = "Property"
        basesensordescription.field.longitude.propertyPrefix = "ssn"
        basesensordescription.field.longitude.propertyURI = basesensordescription.namespace + "city#Longitude"
        basesensordescription.field.longitude.unit = basesensordescription.namespace + "unit:degrees"
        basesensordescription.field.longitude.min = 0
        basesensordescription.field.longitude.max = 180
        basesensordescription.field.longitude.dataType = "float"
        basesensordescription.field.vehicleCount.aggregationMethod = None


        basesensordescription.field.latitude.propertyName = "Property"
        basesensordescription.field.latitude.propertyPrefix = "ssn"
        basesensordescription.field.latitude.propertyURI = basesensordescription.namespace + "city#Latitude"
        basesensordescription.field.latitude.unit = basesensordescription.namespace + "unit:degrees"
        basesensordescription.field.latitude.min = 0
        basesensordescription.field.latitude.max = 180
        basesensordescription.field.latitude.dataType = "float"
        basesensordescription.field.vehicleCount.aggregationMethod = None


        basesensordescription.field.timestamp.propertyName = "MeasuredTime"
        basesensordescription.field.timestamp.propertyURI = basesensordescription.namespace + "city#MeasuredTime"
        basesensordescription.field.timestamp.unit = basesensordescription.namespace + "unit:time"
        basesensordescription.field.timestamp.min = "2012-01-01T00:00:00"
        basesensordescription.field.timestamp.max = "2099-12-31T23:59:59"
        basesensordescription.field.timestamp.dataType = "datetime.datetime"
        basesensordescription.field.timestamp.format = "%Y-%m-%d %H:%M:%S"
        basesensordescription.field.timestamp.skip_annotation = True

        basesensordescription.timestamp.inField = "timestamp"
        basesensordescription.timestamp.format = "%Y-%m-%d %H:%M:%S"

        for point in metadata:
            sensordescription = basesensordescription.deepcopy()
            sensordescription.sensorName = "aarhus_pollution_" + point["id"]
            sensordescription.sensorID = str(point["id"])
            sensordescription.fullSensorID = basesensordescription.namespace + "sensor/Aarhus-Pollution-" + sensordescription.sensorID
            sensordescription.location = "POINT(%(long)s %(lat)s)" % point
            sensordescription.messagebus.routingKey = "Aarhus.Pollution." + sensordescription.sensorID
            self.addWrapper(AarhusPollutionWrapper(sensordescription))