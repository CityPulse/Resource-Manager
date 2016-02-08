# coding=utf-8
__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.history.csvhistory import CSVHistoryReader
from virtualisation.wrapper.parser.csvparser import CSVParser
from virtualisation.wrapper.parser.jsonparser import JSONParser
from virtualisation.misc.log import Log
from virtualisation.wrapper.connection.httpconnection import HttpPullConnection
# from virtualisation.wrapper.splitter.abstractsplitter import AbstractSplitter

import os.path
import uuid
import urllib

def niceFilename(org):
    return org.replace('(', '_').replace(')', '_').replace(' ', '_').replace('/', '_').lower()

class RomaniaWeatherConnection(HttpPullConnection):
    def __init__(self, wrapper):
        super(RomaniaWeatherConnection, self).__init__(wrapper)

    def next(self):
        data = super(RomaniaWeatherConnection, self).next()
        if not data or data.strip() == "Measurement not available":
            return None
        else:
            return data

class InternalWeatherAWWrapper(AbstractWrapper):
    def __init__(self, sensorDescription):
        super(InternalWeatherAWWrapper, self).__init__()
        self.sensorDescription = sensorDescription
        self.parser = JSONParser(self)
        self.connection = RomaniaWeatherConnection(self)

    def getSensorDescription(self):
        return self.sensorDescription

    def start(self):
        if self.replaymode:
            try:
                self.historyreader = CSVHistoryReader(self, AbstractWrapper.getFileObject(__file__, os.path.join("historicdata", "weatherAW-%s.csv" % self.sensorDescription.sensorID), "rU"), delimiter=';')
                self.historyparser = CSVParser(self, self.historyreader.headers)
            except Exception as e:
                Log.e(e)
                self.historyreader = None
        super(InternalWeatherAWWrapper, self).start()

class RomanianWeatherAWWrapper(AbstractComposedWrapper):
    def __init__(self):
        super(RomanianWeatherAWWrapper, self).__init__()

        basesensordescription = SensorDescription()
        basesensordescription.namespace = "http://ict-citypulse.eu/"
        basesensordescription.author = "cityofbrasov"
        basesensordescription.sensorType = "Romanian_Weather"
        basesensordescription.graphName = "romanian_weather#"
        basesensordescription.sourceType = "pull_http"
        basesensordescription.sourceFormat = "application/json"
        basesensordescription.information = "Weather data of Romania"
        basesensordescription.countryName = "Romania"
        basesensordescription.movementBuffer = 3
        basesensordescription.updateInterval = 60 * 60
        basesensordescription.maxLatency = 2
        basesensordescription.fields = ["aqisitionStation", "precipitations", "temperature", "timestamp", "wind"]

        basesensordescription.field.aqisitionStation.propertyName = "Property"
        basesensordescription.field.aqisitionStation.propertyPrefix = "ssn"
        basesensordescription.field.aqisitionStation.propertyURI = basesensordescription.namespace + "romania/weather#Station"
        basesensordescription.field.aqisitionStation.min = ""
        basesensordescription.field.aqisitionStation.max = ""
        basesensordescription.field.aqisitionStation.dataType = "str"
        basesensordescription.field.aqisitionStation.showOnCityDashboard = True

        basesensordescription.field.precipitations.propertyName = "Property"
        basesensordescription.field.precipitations.propertyPrefix = "ssn"
        basesensordescription.field.precipitations.propertyURI = \
            basesensordescription.namespace + "romania/weather#Precipitation"
        basesensordescription.field.precipitations.unit = basesensordescription.namespace + "unit:millimeter"
        basesensordescription.field.precipitations.min = 0
        basesensordescription.field.precipitations.max = 100
        basesensordescription.field.precipitations.dataType = "float"
        basesensordescription.field.precipitations.showOnCityDashboard = True
        basesensordescription.field.precipitations.aggregationMethod = "sax"
        basesensordescription.field.precipitations.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}

        basesensordescription.field.temperature.propertyName = "Temperature"
        basesensordescription.field.temperature.propertyURI = basesensordescription.namespace + "romania/weather#Temperature"
        basesensordescription.field.temperature.unit = basesensordescription.namespace + "unit:degreecelsius"
        basesensordescription.field.temperature.min = -40
        basesensordescription.field.temperature.max = 70
        basesensordescription.field.temperature.dataType = "int"
        basesensordescription.field.temperature.showOnCityDashboard = True
        basesensordescription.field.temperature.aggregationMethod = "sax"
        basesensordescription.field.temperature.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}

        basesensordescription.field.wind.propertyName = "WindSpeed"
        basesensordescription.field.wind.propertyURI = basesensordescription.namespace + "romania/weather#WindSpeed"
        basesensordescription.field.wind.unit = basesensordescription.namespace + "unit:km-per-hour"
        basesensordescription.field.wind.min = 0
        basesensordescription.field.wind.max = 50
        basesensordescription.field.wind.dataType = "int"
        basesensordescription.field.wind.showOnCityDashboard = True
        basesensordescription.field.wind.aggregationMethod = "sax"
        basesensordescription.field.wind.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}

        basesensordescription.field.timestamp.propertyName = "MeasuredTime"
        basesensordescription.field.timestamp.propertyURI = basesensordescription.namespace + "city#MeasuredTime"
        basesensordescription.field.timestamp.unit = basesensordescription.namespace + "unit:time"
        basesensordescription.field.timestamp.min = 0
        basesensordescription.field.timestamp.max = 9999999999999
        basesensordescription.field.timestamp.dataType = "long"
        basesensordescription.field.timestamp.skip_annotation = True

        basesensordescription.timestamp.inField = "timestamp"
        basesensordescription.timestamp.format = "UNIX5"

        locations = {
            "Arad": "POINT(21.31 46.19)",
            "Bacau": "POINT(26.91 46.57)",
            "Baia Mare": "POINT(23.57 47.65)",
            "Barlad": "POINT(27.67 46.23)",
            "Bistrita": "POINT(24.04 45.19)",
            "Botosani": "POINT(26.67 47.75)",
            "Braila": "POINT(27.97 45.28)",
            "Brasov": "POINT(25.60 45.65)",
            "Bucuresti": "POINT(26.1 44.44)",
            "Buzau": "POINT(26.82 45.15)",
            "Calarasi": "POINT(23.85 46.48)",
            "Cluj-Napoca": "POINT(23.61 46.78)",
            "Constanta": "POINT(28.63 44.18)",
            "Craiova": "POINT(23.8 44.32)",
            "Deva": "POINT(22.9 45.88)",
            "Drobeta Turnu Severin": "POINT(22.66 44.63)",
            "Focsani": "POINT(27.18 45.69)",
            "Galati": "POINT(28.04 45.44)",
            "Iasi": "POINT(27.58 47.16)",
            "Ploiesti": "POINT(26.02 44.94)",
            "Piatra-Neamt": "POINT(26.37 46.93)",
            "Ramnicu Valcea": "POINT(24.37 45.10)",
            "Roman": "POINT(26.92 46.92)",
            "Satu Mare": "POINT(22.88 47.78)",
            "Sibiu": "POINT(24.15 45.79)",
            "Slatina": "POINT(24.36 44.42)",
            "Suceava": "POINT(26.15 47.60)",
            "Targu-Mures": "POINT(24.55 46.54)",
            "Timisoara": "POINT(21.23 45.76)",
            "Tulcea": "POINT(28.79 45.17)"
        }

        for _id in locations:
            sensordescription = basesensordescription.deepcopy()
            sensordescription.source = "http://www.bamct.siemens.ro:9000/brasovDataCollector/AccuWeatherView?location=" + urllib.quote_plus(_id)
            sensordescription.sensorName = "romania_weather_aw_%s" % (niceFilename(_id),)
            sensordescription.sensorID = niceFilename(_id)
            sensordescription.fullSensorID = basesensordescription.namespace + "romania/weather/aw/" + niceFilename(sensordescription.sensorID)
            sensordescription.location = locations[_id]

            # One message bus routingkey for each sensorid
            sensordescription.messagebus.routingKey = "Romania.Weather." + sensordescription.sensorID
            self.addWrapper(InternalWeatherAWWrapper(sensordescription))

