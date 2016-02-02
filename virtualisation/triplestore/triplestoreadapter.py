from abc import abstractmethod
from abc import ABCMeta

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


class TripleStoreAdapter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def graphExists(self, graphName):
        pass

    @abstractmethod
    def createGraph(self, graphName):
        pass

    @abstractmethod
    def saveTriple(self, graphName, subject, predicate, object):
        pass

    @abstractmethod
    def saveGraph(self, graph, graphName):
        pass

    @abstractmethod
    def saveMultipleGraphs(self, serialisedGraph, graphName):
        pass

    @abstractmethod
    def getObservationGraph(self, graphName, sensor, start, end, asGraph):
        pass

    @abstractmethod
    def deleteGraph(self, graphName):
        pass

    @abstractmethod
    def getLastQoIData_List(self, graphName, sensorName):
        pass

    @abstractmethod
    def getStreamMinMaxDate(self, graphName, sensorName):
        pass