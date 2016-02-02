from datetime import datetime

__author__ = ['sefki', 'Marten Fischer (m.fischer@hs-osnabrueck.de)', 'Daniel Puschmann']

from virtualisation.aggregation.sax.sax import Sax
import numpy as np
# from CityPulse.VirtuosoConnection.SPARQLQueries import Queries
# import rdflib
# from CityPulse.DataWrappers.SensorWriter import SensorWriter
# from CityPulse.VirtuosoConnection.SPARQLQueries import Queries
# from virtualisation.triplestore.threadedvirtuosowriter import ThreadedTriplestoreAdapter

from virtualisation.misc.buffer import RingBuffer
from virtualisation.aggregation.abstractaggregationcontrol import AbstractAggregationControl
from datetime import timedelta


class SaxControl(AbstractAggregationControl):
    def __init__(self, aggregation_configuration):

        self.buffer = []
        self.saxobj = Sax(aggregation_configuration.alphabet_size)
        self.word_length = aggregation_configuration.word_length
        if aggregation_configuration.unit_of_window is 'hours':
            self.window_size = timedelta(hours=aggregation_configuration.window_duration)
        elif aggregation_configuration.unit_of_window is 'minutes':
            self.window_size = timedelta(minutes=aggregation_configuration.window_duration)
        elif aggregation_configuration.unit_of_window is 'days':
            self.window_size = timedelta(days=aggregation_configuration.window_duration)



    def control(self, data):
        if len(self.buffer) is 0:
            """
            In this case we start a new SAX pattern, so we save the time_stamp
            """
            self.start_time = datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S')
        self.buffer.append(float(data.value))
        if self.start_time + self.window_size > datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S'):
            return None
        result = self.saxobj.sax(self.filterConvert(self.buffer), self.word_length)
        start = self.start_time
        end = datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S')
        size = len(self.buffer)
        self.buffer = []
        self.start_time = datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S')
        return result[0], start, end, size
        # if not result or len(result) == 0:
        #     return None
        # else:
        #     return result[0]

        
        # if len(result) != 0 and list(str(result))[-3] != list(str(result))[-4]:
        """
        @Sefki: If I'm not mistaken you want to compare the last two elements here?! At least the whats
        going to happen in my version. Just a bit more efficient.
        @Sefki, Marten: The output of SAX is a pattern (i.e. SAX word) of a fixed or dynamic size made out of
        individual letters taken from a given alphabet size. Here you are just returning the latest letter of the
        pattern, resulting in more information getting lost.
        """
        # if len(result) != 0 and len(result[0]) >= 2 and result[0][-2] != result[0][-1]:
        #     # print "There is a change in the sax letters"
        #     # print list(str(result))[-4]
        #     # print list(str(result))[-3]
        #     return result[0][-2]



# class SaxControl:
#     def __init__(self):
#         self.graph_uri = "http://ict-citypulse.eu/city#"
#         # saxobj= sax()
#
#         query = Queries()
#         self.AvgSpdList = self.filterConvert(query.getAllSensorObservations("AverageSpeed", "Aarhus_Road_Traffic"))
#         self.VcCntList = self.filterConvert(query.getAllSensorObservations("VehicleCount", "Aarhus_Road_Traffic"))
#         # self.ParkingVcCntList=self.filterConvert(query.getAllSensorObservations("VehicleCount","Aarhus_Parking"))
#         self.ParkingVacancyList = self.filterConvert(query.getAllSensorObservations("ParkingVacancy", "Aarhus_Parking"))
#
#     def saxControl(self, data, propertyName, serviceCategoryName):
#
#         result = []
#
#         if propertyName == self.graph_uri + "VehicleCount" and serviceCategoryName == "Aarhus_Road_Traffic":
#             self.VcCntList = np.append(self.VcCntList, data)
#             print data
#             print self.VcCntList
#             saxobj = Sax()
#             result = saxobj.sax(self.VcCntList, len(self.VcCntList))
#         if propertyName == self.graph_uri + "AverageSpeed" and serviceCategoryName == "Aarhus_Road_Traffic":
#             self.AvgSpdList = np.append(self.AvgSpdList, data)
#             print data
#             print self.AvgSpdList
#             saxobj = Sax()
#             result = saxobj.sax(self.AvgSpdList, len(self.AvgSpdList))
#         if propertyName == self.graph_uri + "ParkingVacancy" and serviceCategoryName == "Aarhus_Parking":
#             self.ParkingVacancyList = np.append(self.ParkingVacancyList, data)
#             print data
#             print self.ParkingVacancyList
#             saxobj = Sax()
#             result = saxobj.sax(self.ParkingVacancyList, len(self.ParkingVacancyList))
#
#         if len(result) == 0:
#             return None
#
#         if len(result) != 0 and list(str(result))[-3] == list(str(result))[-4]:
#             print "There is no change in the sax letters"
#             print list(str(result))[-4]
#             print list(str(result))[-3]
#
#         if len(result) != 0 and list(str(result))[-3] != list(str(result))[-4]:
#             print "There a change in the sax letters"
#             print list(str(result))[-4]
#             print list(str(result))[-3]
#             return list(str(result))[-3]
#         return None

    def test(self):
        saxobj = Sax()
        # data=[1,2,3,6,7,10,12]
        data = np.random.random((150000, 1))
        result = saxobj.sax(data, len(data))
        print result
        print list(str(result))[-3]
        if list(str(result))[-3] == list(str(result))[-4]:
            print "There is no change in the data"

        if list(str(result))[-3] != list(str(result))[-4]:
            print "There a change in the data"

    def filterConvert(self, aList):
        # aList = filter(None, aList)
        aList = np.asarray(aList)
        return aList
