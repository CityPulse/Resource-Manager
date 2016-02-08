# coding=utf-8
__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.history.csvhistory import CSVHistoryReader
from virtualisation.wrapper.parser.csvparser import CSVParser
from virtualisation.wrapper.parser.jsonparser import JSONParser
from virtualisation.misc.log import Log
from virtualisation.wrapper.connection.httpconnection import HttpPullConnection

import os.path
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

class InternalWeatherMRWrapper(AbstractWrapper):
    def __init__(self, sensorDescription):
        super(InternalWeatherMRWrapper, self).__init__()
        self.sensorDescription = sensorDescription
        self.parser = JSONParser(self)
        self.connection = RomaniaWeatherConnection(self)

    def getSensorDescription(self):
        return self.sensorDescription

    def start(self):
        try:
            if self.replaymode:
                fobj = AbstractWrapper.getFileObject(__file__, os.path.join("historicdata", "weatherMR-%s.csv" % niceFilename(self.sensorDescription.sensorID)), "rU")
                self.historyreader = CSVHistoryReader(self, fobj, delimiter=';')
                self.historyparser = CSVParser(self, self.historyreader.headers)
        except Exception as e:
            Log.e(e)
            self.historyreader = None
        super(InternalWeatherMRWrapper, self).start()

class RomanianWeatherMRWrapper(AbstractComposedWrapper):
    def __init__(self):
        super(RomanianWeatherMRWrapper, self).__init__()

        basesensordescription = SensorDescription()
        basesensordescription.namespace = "http://ict-citypulse.eu/"
        basesensordescription.author = "cityofbrasov"
        basesensordescription.sensorType = "Romanian_Weather"
        basesensordescription.graphName = "romanian_weather#"
        basesensordescription.sourceType = "pull_http"
        basesensordescription.sourceFormat = "application/json"
        basesensordescription.information = "Weather data of Romania"
        basesensordescription.countryName = "Romania"
        basesensordescription.movementBuffer = 0
        basesensordescription.maxLatency = 2
        basesensordescription.updateInterval = 60 * 60
        basesensordescription.fields = ["aqisitionStation", "pressure", "relative_humidity", "temperature", "timestamp",
                                        "wind", "nebulosityType", "windtyp"]

        basesensordescription.field.aqisitionStation.propertyName = "Property"
        basesensordescription.field.aqisitionStation.propertyPrefix = "ssn"
        basesensordescription.field.aqisitionStation.propertyURI = basesensordescription.namespace + "romania/weather#Station"
        basesensordescription.field.aqisitionStation.min = ""
        basesensordescription.field.aqisitionStation.max = ""
        basesensordescription.field.aqisitionStation.dataType = "str"
        basesensordescription.field.aqisitionStation.showOnCityDashboard = True

        basesensordescription.field.pressure.propertyName = "Property"
        basesensordescription.field.pressure.propertyPrefix = "ssn"
        basesensordescription.field.pressure.propertyURI = \
            basesensordescription.namespace + "romania/weather#Pressure"
        basesensordescription.field.pressure.unit = basesensordescription.namespace + "unit:mmHG"
        basesensordescription.field.pressure.min = 500
        basesensordescription.field.pressure.max = 1500
        basesensordescription.field.pressure.dataType = "float"
        basesensordescription.field.pressure.showOnCityDashboard = True
        basesensordescription.field.pressure.aggregationMethod = "sax"
        basesensordescription.field.pressure.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.temperature.propertyName = "Temperature"
        basesensordescription.field.temperature.propertyURI = basesensordescription.namespace + "romania/weather#Temperature"
        basesensordescription.field.temperature.unit = basesensordescription.namespace + "unit:degreecelsius"
        basesensordescription.field.temperature.min = -40
        basesensordescription.field.temperature.max = 70
        basesensordescription.field.temperature.dataType = "float"
        basesensordescription.field.temperature.showOnCityDashboard = True
        basesensordescription.field.temperature.aggregationMethod = "sax"
        basesensordescription.field.temperature.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.wind.propertyName = "WindSpeed"
        basesensordescription.field.wind.propertyURI = basesensordescription.namespace + "romania/weather#WindSpeed"
        basesensordescription.field.wind.unit = basesensordescription.namespace + "unit:km-per-hour"
        basesensordescription.field.wind.min = 0
        basesensordescription.field.wind.max = 12
        basesensordescription.field.wind.dataType = "int"
        basesensordescription.field.wind.showOnCityDashboard = True
        basesensordescription.field.wind.aggregationMethod = "sax"
        basesensordescription.field.wind.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.relative_humidity.propertyName = "Property"
        basesensordescription.field.relative_humidity.propertyPrefix = "ssn"
        basesensordescription.field.relative_humidity.propertyURI = basesensordescription.namespace + "romania/weather#Humidity"
        # TODO unit of measurement?
        basesensordescription.field.relative_humidity.min = 0
        basesensordescription.field.relative_humidity.max = 100
        basesensordescription.field.relative_humidity.dataType = "int"
        basesensordescription.field.relative_humidity.showOnCityDashboard = True
        basesensordescription.field.relative_humidity.aggregationMethod = "sax"
        basesensordescription.field.relative_humidity.aggregationConfiguration = {"alphabet_size": 5, "word_length": 3,
                                                                        "unit_of_window": "hours", "window_duration": 1}


        basesensordescription.field.timestamp.propertyName = "MeasuredTime"
        basesensordescription.field.timestamp.propertyURI = basesensordescription.namespace + "city#MeasuredTime"
        basesensordescription.field.timestamp.unit = basesensordescription.namespace + "unit:time"
        basesensordescription.field.timestamp.min = 0
        basesensordescription.field.timestamp.max = 9999999999999
        basesensordescription.field.timestamp.dataType = "long"
        basesensordescription.field.timestamp.skip_annotation = True

        basesensordescription.field.nebulosityType.propertyName = "Property"
        basesensordescription.field.nebulosityType.propertyPrefix = "ssn"
        basesensordescription.field.nebulosityType.propertyURI = basesensordescription.namespace + "romania/weather#NebulosityType"
        basesensordescription.field.nebulosityType.min = ""
        basesensordescription.field.nebulosityType.max = ""
        basesensordescription.field.nebulosityType.dataType = "str"
        basesensordescription.field.nebulosityType.showOnCityDashboard = True

        basesensordescription.field.windtyp.propertyName = "Property"
        basesensordescription.field.windtyp.propertyPrefix = "ssn"
        basesensordescription.field.windtyp.propertyURI = basesensordescription.namespace + "romania/weather#WindType"
        basesensordescription.field.windtyp.min = ""
        basesensordescription.field.windtyp.max = ""
        basesensordescription.field.windtyp.dataType = "str"
        basesensordescription.field.windtyp.showOnCityDashboard = True

        basesensordescription.timestamp.inField = "timestamp"
        basesensordescription.timestamp.format = "UNIX5"

        locations = {
            "ADAMCLISI": "POINT(27.96 44.09)",
            "ADJUD": "POINT(27.18 46.1)",
            "ALBA IULIA": "POINT(23.57 46.07)",
            "ALEXANDRIA": "POINT(25.33 43.97)",
            "ARAD": "POINT(21.32 46.17)",
            "BACAU": "POINT(26.92 46.58)",
            "BACLES": "POINT(23.12 44.49)",
            "BAIA MARE": "POINT(23.58 47.67)",
            "BAILE HERCULANE": "POINT(22.41 44.88)",
            "BAILESTI": "POINT(23.35 44.03)",
            "BAISOARA": "POINT(23.46 46.58)",
            "BALEA LAC": "POINT(24.61 45.60)",
            "BANLOC": "POINT(21.14 45.39)",
            "BARAOLT": "POINT(25.6 46.08)",
            "BARLAD:": "POINT(27.67 46.23)",
            "BARNOVA RADAR": "POINT(27.63 47.07)",
            "BATOS": "POINT(24.65 46.89)",
            "BECHET": "POINT(24.18 44.39)",
            "BISOCA": "POINT(26.71 45.54)",
            "BISTRITA": "POINT(24.49 47.13)",
            "BLAJ": "POINT(23.91 46.18)",
            "BOITA": "POINT(24.26 45.63)",
            "BOROD": "POINT(22.61 46.99)",
            "BOTOSANI": "POINT(26.67 47.75)",
            "BOZOVICI": "POINT(22.0 44.93)",
            "BRAILA": "POINT(27.96 45.27)",
            "BRASOV GHIMBAV": "POINT(25.51 45.66)",
            "BUCIN": "POINT(25.42 46.68)",
            "BUCURESTI AFUMATI": "POINT(26.25 44.53)",
            "BUCURESTI BANEASA": "POINT(26.08 44.49)",
            "BUCURESTI FILARET": "POINT(26.08 44.42)",
            "BUZAU": "POINT(26.82 45.15)",
            "CALAFAT": "POINT(22.94 43.99)",
            "CALARASI": "POINT(27.34 44.2)",
            "CALIMANI RETITIS": "POINT(25.24 47.09)",
            "CAMPENI BISTRA": "POINT(23.05 46.36)",
            "CAMPINA": "POINT(25.74 45.13)",
            "CAMPULUNG MUSCEL": "POINT(25.05 45.27)",
            "CARACAL": "POINT(24.35 44.11)",
            "CARANSEBES": "POINT(22.22 45.42)",
            "CEAHLAU TOACA": "POINT(25.95 46.98)",
            "CERNAVODA": "POINT(28.03 44.34)",
            "CHISINEU CRIS": "POINT(21.52 46.52)",
            "CLUJ-NAPOCA": "POINT(23.58 46.76)",
            "CONSTANTA": "POINT(28.64 44.17)",
            "CORUGEA": "POINT(28.34 44.74)",
            "COTNARI": "POINT(26.94 47.35)",
            "CRAIOVA": "POINT(23.8 44.32)",
            "CUNTU": "POINT(24.14 45.59)",
            "CURTEA DE ARGES": "POINT(24.68 45.14)",
            "DARABANI": "POINT(28.3 43.79)",
            "DEDULES": None,
            "DEDULESTI-MORARESTI": "POINT(24.53 45.01)",
            "DEJ": "POINT(23.88 47.14)",
            "DEVA": "POINT(22.9 45.88)",
            "DRAGASANI": "POINT(24.26 44.66)",
            "DROBETA TURNU SEVERIN": "POINT(22.67 44.63)",
            "DUMBRAVENI": "POINT(24.58 46.23)",
            "DUMBRAVITA DE CODRU": "POINT(22.16 46.66)",
            "FAGARAS": "POINT(24.97 45.84)",
            "FETESTI": "POINT(27.83 44.37)",
            "FOCSANI": "POINT(27.18 45.7)",
            "FUNDATA": "POINT(25.29 45.44)",
            "FUNDULEA": "POINT(26.52 44.45)",
            "GALATI": "POINT(28.04 45.42)",
            "GIURGIU": "POINT(25.97 43.9)",
            "GORGOVA": "POINT(29.17 45.18)",
            "GRIVITA": "POINT(27.65 45.72)",
            "GURA PORTITEI": "POINT(29.00 44.69)",
            "GURAHONT": "POINT(22.34 46.27)",
            "HALANGA": "POINT(22.69 44.68)",
            "HARSOVA": "POINT(27.95 44.69)",
            "HOLOD": "POINT(22.13 46.79)",
            "HUEDIN": "POINT(23.03 46.87)",
            "IASI": "POINT(27.59 47.16)",
            "IEZER": "POINT(26.34 47.99)",
            "INTORSURA BUZAULUI": "POINT(26.03 45.67)",
            "JIMBOLIA": "POINT(20.72 45.79)",
            "JOSENI": "POINT(25.5 46.7)",
            "JURILOVCA": "POINT(28.87 44.76)",
            "LACAUTI": "POINT(26.02 44.93)",
            "LUGOJ": "POINT(21.9 45.69)",
            "MAHMUDIA": "POINT(29.08 45.08)",
            "MANGALIA": "POINT(28.58 43.82)",
            "MEDGIDIA": "POINT(28.27 44.25)",
            "MIERCUREA CIUC": "POINT(25.81 46.36)",
            "MOLDOVA VECHE": "POINT(21.62 44.72)",
            "NEGRESTI VASLUI": "POINT(27.46 46.83)",
            "OBARSIA LOTRULUI": "POINT(23.63 45.44)",
            "OCNA SUGATAG": "POINT(23.93 47.78)",
            "ODORHEIUL SECUIESC": "POINT(25.29 46.3)",
            "OLTENITA": "POINT(26.64 44.09)",
            "ORADEA": "POINT(21.92 47.07)",
            "ORAVITA": "POINT(21.68 45.03)",
            "PADES APA NEAGRA": "POINT(22.86 45.0)",
            "PALTINIS": "POINT(23.93 45.66)",
            "PARANG": "POINT(23.56 45.34)",
            "PATARLAGELE": "POINT(26.36 45.32)",
            "PENTELEU": "POINT(26.41 45.60)",
            "PETROSANI": "POINT(23.37 45.42)",
            "PIATRA NEAMT": "POINT(26.37 46.93)",
            "PITESTI": "POINT(24.88 44.86)",
            "PLOIESTI": "POINT(26.02 44.94)",
            "POIANA STAMPEI": "POINT(25.14 47.32)",
            "POLOVRAGI": "POINT(23.81 45.17)",
            "PREDEAL": "POINT(25.58 45.5)",
            "RADAUTI": "POINT(25.92 47.84)",
            "RAMNICU SARAT": "POINT(27.06 45.38)",
            "RAMNICU VALCEA": "POINT(24.38 45.1)",
            "RESITA": "POINT(21.89 45.3)",
            "ROMAN": "POINT(26.92 46.92)",
            "ROSIA MONTANA": "POINT(23.13 46.31)",
            "ROSIORII DE VEDE": "POINT(24.99 44.11)",
            "SACUIENI": "POINT(22.11 47.34)",
            "SANNICOLAU MARE": "POINT(20.63 46.07)",
            "SARMASU": "POINT(24.16 46.75)",
            "SATU MARE": "POINT(22.88 47.8)",
            "SEBES ALBA": "POINT(23.57 45.96)",
            "SEMENIC": "POINT(21.96 45.15)",
            "SFANTU GHEORGHE DELTA": "POINT(29.59 44.9)",
            "SFANTU GHEORGHE MUNTE": None,
            "SIBIU": "POINT(24.15 45.79)",
            "SIGHETUL MARMATIEI": "POINT(23.89 47.93)",
            "SINAIA 1500": "POINT(24.33 46.16)",
            "SIRIA": "POINT(21.63 46.26)",
            "SLATINA": "POINT(24.37 44.42)",
            "SLOBOZIA": "POINT(27.37 44.56)",
            "STANA DE VALE": "POINT(26.08 44.41)",
            "STEFANESTI STANCA": "POINT(27.2 47.82)",
            "STEI PETRU GROZA": "POINT(22.47 46.53)",
            "STOLNICI": "POINT(24.78 44.57)",
            "SUCEAVA": "POINT(26.26 47.65)",
            "SULINA": "POINT(29.65 45.16)",
            "SUPURU DE JOS": "POINT(22.79 47.47)",
            "TARCU": None,
            "TARGOVISTE": "POINT(21.83 45.82)",
            "TARGU JIU": "POINT(23.28 45.04)",
            "TARGU LAPUS": "POINT(23.86 47.45)",
            "TARGU LOGRESTI": "POINT(23.71 44.87)",
            "TARGU MURES": "POINT(24.56 46.54)",
            "TARGU NEAMT": "POINT(26.36 47.2)",
            "TARGU OCNA": "POINT(26.62 46.28)",
            "TARGU SECUIESC": "POINT(26.14 46.0)",
            "TARNAVENI BOBOHALMA": "POINT(24.24 46.35)",
            "TEBEA": "POINT(22.73 46.17)",
            "TECUCI": "POINT(27.43 45.85)",
            "TIMISOARA": "POINT(21.23 45.76)",
            "TITU": "POINT(25.57 44.66)",
            "TOPLITA": "POINT(25.35 46.92)",
            "TULCEA": "POINT(28.79 45.17)",
            "TURDA": "POINT(23.79 46.57)",
            "TURNU MAGURELE": "POINT(24.87 43.75)",
            "URZICENI": "POINT(26.64 44.72)",
            "VARADIA DE MURES": "POINT(22.16 46.01)",
            "VARFUL OMU": "POINT(25.45 45.44)",
            "VASLUI": "POINT(27.73 46.64)",
            "VIDELE": "POINT(25.53 44.28)",
            "VLADEASA 1400": None,
            "VLADEASA 1800": "POINT(24.51 46.52)",
            "VOINEASA": "POINT(23.96 45.42)",
            "ZALAU": "POINT(23.05 47.18)",
            "ZIMNICEA": "POINT(25.37 43.65)"
        }

        for _id in locations:
            sensordescription = basesensordescription.deepcopy()
            sensordescription.source = "http://www.bamct.siemens.ro:9000/brasovDataCollector/MeteoRomaniaView?location=" + urllib.quote_plus(_id)
            sensordescription.sensorName = "romania_weather_mr_%s" % (niceFilename(_id),)
            sensordescription.sensorID = "%s" % (_id,)
            sensordescription.fullSensorID = basesensordescription.namespace + "romania/weather/mr/" + niceFilename(sensordescription.sensorID)
            sensordescription.location = locations[sensordescription.sensorID] if locations[sensordescription.sensorID] else "POINT(25.600581 45.654376)"
            sensordescription.messagebus.routingKey = "Romania.Weather." + sensordescription.sensorID
            self.addWrapper(InternalWeatherMRWrapper(sensordescription))
