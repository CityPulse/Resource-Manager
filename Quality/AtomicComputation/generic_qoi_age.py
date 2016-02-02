from datetime import timedelta
import datetime
import logging

from Quality.AtomicComputation.reputationsystem.qoimetric import QoIMetric
from Quality.AtomicComputation.reputationsystem.repsys import ReputationSystem
from Quality.AtomicComputation.reputationsystem.rewardpunishment import RewardAndPunishment
from virtualisation.clock.abstractclock import AbstractClock
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L


class Age(QoIMetric):
    """docstring for Age"""

    def __init__(self):
        QoIMetric.__init__(self, "Age")
        self.lastUpdate = None
        self.weight = 0.99
        self.nulldelta = timedelta(seconds=0)
        self.rewardAndPunishment = RewardAndPunishment(5)
        self.datatype = "time"
        self.updatecounter = 1
        self.unit = "http://purl.oclc.org/NET/muo/ucum/unit/time/second"

    def updateDescription(self):
        # get data from sensor description
        # 		self.maxAge = timedelta(seconds=self.repsys.description.updateInterval)
        self.annotatedAge = self.repsys.description.updateInterval # + 0.05 * self.repsys.description.updateInterval

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

        samplingTime = datetime.datetime.strptime(data[data.fields[0]].observationSamplingTime,
                                                  AbstractClock.parserformat)

        age = (samplingTime - ts).total_seconds()
#         print "age:", age, "ts", ts, "sampling", samplingTime

        if self.lastUpdate == None:
            self.lastUpdate = ts
            self.rewardAndPunishment.update(True)
            self.absoluteValue = age
            self.ratedValue = 1.0
            self.min = age
            self.mean = age
        else:
            # 			delta = ts - self.lastUpdate
            self.lastUpdate = ts
            if data.recovered:
                self.rewardAndPunishment.update(False)
            else:
                self.rewardAndPunishment.update(age <= self.annotatedAge)

            # 			delay = delta.days * 86400 + delta.seconds
            self.absoluteValue = age
            self.ratedValue = self.rewardAndPunishment.value()
            age = float(age)
            self.min = min(self.min, age)
            self.mean = ((self.updatecounter - 1) * self.mean) / self.updatecounter + age / self.updatecounter

        ageReturn = JSONObject()

        ageReturn.absoluteValue = self.absoluteValue
        ageReturn.ratedValue = self.ratedValue
        ageReturn.unit = self.unit
        return (self.name, ageReturn)
