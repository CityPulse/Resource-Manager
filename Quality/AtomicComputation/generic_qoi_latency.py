# coding=utf-8
__author__ = 'Thorben Iggena (t.iggena@hs-osnabrueck.de)'

from datetime import timedelta
import logging

from Quality.AtomicComputation.reputationsystem.qoimetric import QoIMetric
from Quality.AtomicComputation.reputationsystem.repsys import ReputationSystem
from Quality.AtomicComputation.reputationsystem.rewardpunishment import RewardAndPunishment
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L

class Latency(QoIMetric):
    """docstring for Latency"""

    def __init__(self):
        QoIMetric.__init__(self, "Latency")
        self.lastUpdate = None
        self.weight = 0.99
        self.nulldelta = timedelta(seconds=0)
        self.rewardAndPunishment = RewardAndPunishment(5)
        self.datatype = "time"
        self.updatecounter = 1
        self.unit = "http://purl.oclc.org/NET/muo/ucum/unit/time/second"

    def updateDescription(self):
        # get data from sensor description
        self.maxAge = timedelta(seconds=self.repsys.description.updateInterval)
        self.definedAge = self.repsys.description.updateInterval

    def update(self, data):
        self.updateDescription()

        # special case when no fields are in data
        # (fault recovery is not ready yet)
        if len(data.fields) == 0:
            self.rewardAndPunishment.update(False)
            self.absoluteValue = float("inf")
            self.ratedValue = self.rewardAndPunishment.value()
            return

        ts = self.repsys.timestamp

        self.updatecounter += 1

        latency = data.latency

        annotatedLatency = self.repsys.description.maxLatency

        if self.lastUpdate is None:
            self.lastUpdate = ts
            self.rewardAndPunishment.update(True)
            self.absoluteValue = latency
            self.ratedValue = 1.0
            self.min = latency
            self.mean = latency
        else:
            self.lastUpdate = ts
            
            if data.recovered:
                self.rewardAndPunishment.update(False)
            else:
                self.rewardAndPunishment.update(annotatedLatency > latency)

            self.absoluteValue = latency
            self.ratedValue = self.rewardAndPunishment.value()
            self.min = min(self.min, latency)
            self.mean = ((self.updatecounter - 1) * self.mean) / self.updatecounter + latency / self.updatecounter

        lat = JSONObject()

        lat.absoluteValue = self.absoluteValue
        lat.ratedValue = self.ratedValue
        lat.unit = self.unit
        return (self.name, lat)
# print "latency:", self.absoluteValue, "latency2:", self.ratedValue, "latency_annotated:", annotatedLatency
