from datetime import timedelta

from Quality.AtomicComputation.reputationsystem.qoimetric import QoIMetric
from Quality.AtomicComputation.reputationsystem.repsys import ReputationSystem
from Quality.AtomicComputation.reputationsystem.rewardpunishment import RewardAndPunishment
from virtualisation.clock.abstractclock import AbstractClock
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L

class Frequency(QoIMetric):
    """docstring for Frequency"""

    def __init__(self):
        QoIMetric.__init__(self, "Frequency")
        self.frequencyQoI = 1.0
        self.lastUpdate = None
        self.weight = 0.99
        self.nulldelta = timedelta(seconds=0)
        self.rewardAndPunishment = RewardAndPunishment(20)
        self.updatecounter = 0
        self.unit = "http://purl.oclc.org/NET/muo/ucum/unit/frequency/Herz"

    def updateDescription(self):
        # get data from sensor description
        self.definedFreq = self.repsys.description.updateInterval
        self.goalFrequency = timedelta(seconds=self.repsys.description.updateInterval) #+ 0.05 * self.repsys.description.updateInterval)

    def nonValueUpdate(self):
        # 		print "Frequency nonValueUpdate"
        self.calculateFrequency(self.repsys.timestamp, False)
        freq = JSONObject()
        freq.absoluteValue = self.absoluteValue
        freq.ratedValue = self.ratedValue
        freq.unit = self.unit
        return (self.name, freq)

    def update(self, data):
        # special case when no fields are in data
        # (fault recovery is not ready yet)
        if len(data.fields) == 0:
            self.rewardAndPunishment.update(False)
            self.absoluteValue = float("inf")
            self.ratedValue = self.rewardAndPunishment.value()
            return

        ts = self.repsys.timestamp
        self.calculateFrequency(ts, data.recovered)

        freq = JSONObject()

        freq.absoluteValue = self.absoluteValue
        freq.ratedValue = self.ratedValue
        freq.unit = self.unit
        return (self.name, freq)

    def calculateFrequency(self, ts, recovered):
        self.updateDescription()

        self.updatecounter += 1

        if self.lastUpdate == None:
            self.lastUpdate = ts
            self.rewardAndPunishment.update(True)
            self.min = self.definedFreq
            self.mean = self.definedFreq
        # 			return (self.definedFreq, self.rewardAndPunishment.value())
        else:
            delta = ts - self.lastUpdate
            self.lastUpdate = ts
            if recovered:
                self.rewardAndPunishment.update(False)
            else:
                self.rewardAndPunishment.update((delta > self.nulldelta and delta <= self.goalFrequency))

            delay = delta.days * 86400 + delta.seconds
#             print "delay", delay, "for sensor", self.repsys.description.fullSensorID

            if delay > 0:
                self.absoluteValue = 1.0 / delay
                self.min = min(self.min, self.absoluteValue)
                self.mean = ((
                             self.updatecounter - 1) * self.mean) / self.updatecounter + self.absoluteValue / self.updatecounter
            else:
                self.absoluteValue = float("inf")
            self.ratedValue = self.rewardAndPunishment.value()

# print "frequency:", self.absoluteValue, "frequency2:", self.ratedValue, "frequency_annotated:", self.goalFrequency
