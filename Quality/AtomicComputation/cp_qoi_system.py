# coding=utf-8
from Quality.AtomicComputation.BlackHole import BlackHoleSink
from Quality.AtomicComputation.CSVSink import CSVSink
from Quality.AtomicComputation.generic_qoi_age import Age
from Quality.AtomicComputation.generic_qoi_completeness import Completeness
from Quality.AtomicComputation.generic_qoi_correctness import Correctness
from Quality.AtomicComputation.generic_qoi_frequency import Frequency
from Quality.AtomicComputation.generic_qoi_latency import Latency
from Quality.AtomicComputation.reputationsystem.repsys import ReputationSystem
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L


__author__ = 'Thorben Iggena (t.iggena@hs-osnabrueck.de)'

# from Quality.AtomicComputation.VirtuosoSink import VirtuosoSink
# from Quality.AtomicComputation.TerminalSink import TerminalSink


class SensorQueueElement(object):
    def __init__(self, description, data):
        self.sensorDescription = description
        self.sensorData = data


class CpQoiSystem(object):

    def __init__(self):
        self.initialised = False
        self.reputationSystem = None
        self.messageBusQueue = None
        L.d2("CpQoiSystem started")

    def getObservationIds(self, data):
        return [data[field].observationID for field in data.fields]

    def addData(self, description, data, clock):
        if not self.initialised:
            self.initialise(description, clock)
        self.reputationSystem.setClock(clock)
        self.reputationSystem.setDescription(description)
        # send data to reputationsystem
        qoiInformation = self.reputationSystem.update(data)
        # persist calculated qoi
        # get list of observationIds for virtuoso sink
        self.reputationSystem.persist(self.getObservationIds(data))
        return qoiInformation

    # initialise reputationsystem with values from sensor description, add qoi metrics and sinks
    def initialise(self, description, clock):
        self.reputationSystem = ReputationSystem(description, clock)
        # self.reputationSystem.addSink(CSVSink())
        # self.reputationSystem.addSink(VirtuosoSink(self.messageBusQueue))
        # self.reputationSystem.addSink(TerminalSink())
        self.reputationSystem.addSink(BlackHoleSink())
        self.reputationSystem.addQoIMetric(Frequency())
        self.reputationSystem.addQoIMetric(Completeness())
        self.reputationSystem.addQoIMetric(Age())
        self.reputationSystem.addQoIMetric(Latency())
        self.reputationSystem.addQoIMetric(Correctness())
        self.initialised = True
        L.d2("CpQoiSystem initialised")

    def setMessageBusQueue(self, messageBusQueue):
        self.messageBusQueue = messageBusQueue
        
    def getLastQoI(self, types=None, avg=None, minimum=None, maximum=None):
        qoiData = JSONObject()
        for metric in self.reputationSystem.metrics:
            q = JSONObject()
            currentValues = JSONObject()
            currentValues.absoluteValue = metric.absoluteValue
            currentValues.ratedValue = metric.ratedValue
            q.unit = metric.unit
            qoiData[metric.name] = q
            q.CURRENT = currentValues
            if types:
                self.reputationSystem.avgQoIManager.getValues(q, metric.name, types, avg, minimum, maximum)
        return qoiData


