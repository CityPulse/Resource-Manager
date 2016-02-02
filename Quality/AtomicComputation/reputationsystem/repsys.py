import datetime

from Quality.Average.averageQuality import DAILY
from Quality.Average.averageQualityManager import AverageQualityManager
from qoimetric import QoIMetric
from virtualisation.clock.abstractclock import AbstractClock
from virtualisation.misc.log import Log as L


class ReputationSystem(object):
    """docstring for ReputationSystem"""

    def __init__(self, description, clock):
        self.metrics = []
        self.setDescription(description)
        self.sinkList = []
        self.timestamp = None
        self.clock = clock
        self.jobID = None
        self.addClockJob()
        self.avgQoIManager = AverageQualityManager(description.updateInterval)

    def setClock(self, clock):
        if self.clock is not clock:
            self.clock = clock
            self.jobID = None  # set to none because old jobs are not deleteable anymore

    def addClockJob(self, deleteOldJob=False):
        L.d2("ReputationSystem: addClockJob for Stream", self.description.fullSensorID, "with", self.validationInterval)
        if deleteOldJob and self.jobID:
            self.clock.removeJob(self.jobID)
        self.jobID = self.clock.addJob(self.validationInterval, self.checkTimeRelevantMetrics, args=(self.timestamp),
                                       reoccurring=False)

    def setDescription(self, description):
        self.description = description
        # update validation interval
        self.validationInterval = self.description.updateInterval + self.description.updateInterval * 0.05  # add some extra time to avoid races

    def __del__(self):
        for m in self.metrics:
            del m
        for sink in self.sinkList:
            del sink

    def setSink(self, sink):
        sink.reputationsystem = self
        self.sink = sink

    def addSink(self, sink):
        sink.reputationsystem = self
        self.sinkList.append(sink)

    def addQoIMetric(self, qoiMetric):
        if not isinstance(qoiMetric, QoIMetric):
            raise Exception("not a QoIMetric")
        qoiMetric.repsys = self
        self.metrics.append(qoiMetric)
        for sink in self.sinkList:
            sink.qoiMetricAdded(qoiMetric.name, qoiMetric.initialValue)
        self.avgQoIManager.addQoIMetric(qoiMetric)

    def update(self, data):
        L.d2("ReputationSystem: update called for Stream", self.description.fullSensorID)
        self.setTimestamp(data)
        returnValues = {}
        if data is not None:
            for m in self.metrics:
                value = m.update(data)
                if value:
                    returnValues[value[0]] = value[1]
                for sink in self.sinkList:
                    sink.update(m)
        self.addClockJob(True)
        self.avgQoIManager.calculateAvgQualities(returnValues)
        return returnValues
    
    def persist(self, observationIdList):
        for sink in self.sinkList:
            sink.persist(observationIdList)

    def checkTimeRelevantMetrics(self, lastUpdate):
        L.d("ReputationSystem: checkTimeRelevantMetrics called for Stream", self.description.fullSensorID)
        L.d("ReputationSystem:", lastUpdate, self.timestamp)
        if (lastUpdate is not None) and (lastUpdate == self.timestamp):  # check if there was an update in the meanwhile
            L.d("ReputationSystem: There was no update, lets punish!")
            qoiValues = {}
            for metric in self.metrics:
                value = metric.nonValueUpdate()
                if value:
                    qoiValues[value[0]] = value[1]
                
            self.avgQoIManager.calculateAvgQualities(qoiValues)
        self.addClockJob()

    def setTimestamp(self, data):
        if len(data.fields) != 0:
            self.timestamp = datetime.datetime.strptime(data[data.fields[0]].observationResultTime, AbstractClock.parserformat)

