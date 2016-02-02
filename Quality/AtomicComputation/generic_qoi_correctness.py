import datetime
import logging

from Quality.AtomicComputation.reputationsystem.qoimetric import QoIMetric
from Quality.AtomicComputation.reputationsystem.rewardpunishment import RewardAndPunishment
from virtualisation.clock.abstractclock import AbstractClock
from virtualisation.misc import utils
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L

__author__ = 'Thorben Iggena (t.iggena@hs-osnabrueck.de)'


class Correctness(QoIMetric):
    """docstring for Correctness"""

    def __init__(self):
        QoIMetric.__init__(self, "Correctness")
        self.updatecounter = 0
        self.rewardAndPunishment = RewardAndPunishment(20)
        self.goal = 1  # always want 100% correctness
        self.min = 1
        self.mean = 1
        self.unit = "http://purl.oclc.org/NET/muo/ucum/unit/fraction/percent"

    def update(self, data):
        self.updatecounter += 1

        # special case when no fields are in data
        # (fault recovery is not ready yet)
        if len(data.fields) == 0:
            self.rewardAndPunishment.update(False)
            self.absoluteValue = float("inf")
            self.ratedValue = self.rewardAndPunishment.value()
            return


        wrongFieldList = []
        for field in data.fields:
            if field not in data:
                wrongFieldList.append(field)
                continue

            dataTypeStr = self.repsys.description.field[field].dataType
            dataType = utils.getType(dataTypeStr)
            minValue, maxValue = self.getMinMaxValue(field, data)

            value = data[field].value
            # print "field:", field, "value:", value, "min:", minValue, "max:", maxValue, "dataType:", dataTypeStr, dataType, "value type:", type(value)

            if minValue and maxValue:
                if dataTypeStr == "datetime.datetime":
                    minValue = datetime.datetime.strptime(minValue, AbstractClock.parserformat)
                    maxValue = datetime.datetime.strptime(maxValue, AbstractClock.parserformat)
                else:
                    maxValue = dataType(maxValue)
                    minValue = dataType(minValue)

            # everything might be a string => first check for type, then try to cast, afterwards check min and max
            wrongValue = False
            if not isinstance(value, dataType): # type(value) is not dataType:
                try:
                    # special handling for datetime as format is needed
                    if dataTypeStr == "datetime.datetime":
                        value = datetime.datetime.strptime(value, self.repsys.description.field[field].format)
                    else:
                        value = dataType(value)
                except ValueError:
                    wrongFieldList.append(field)
                    wrongValue = True

            if not wrongValue:
                # now check if value is within min max interval
                if minValue and minValue is not "":
                    if value < minValue:
                        wrongFieldList.append(field)
                elif maxValue and maxValue is not "":
                    if value > maxValue:
                        wrongFieldList.append(field)
# 			print "Correctness for", self.repsys.description.fullSensorID, len(wrongFieldList), value, minValue, maxValue
        L.d("Correctness wrong fields:", len(wrongFieldList), "(", ",".join(wrongFieldList), ")")

        if data.recovered or (len(wrongFieldList) >= 1):
            self.rewardAndPunishment.update(False)
        else:
            self.rewardAndPunishment.update(True)

        self.ratedValue = self.rewardAndPunishment.value()
        self.absoluteValue = 1 - len(wrongFieldList) / len(data.fields)
        self.min = min(self.min, self.absoluteValue)
        self.mean = ((self.updatecounter - 1) * self.mean) / self.updatecounter + float(
            self.absoluteValue) / self.updatecounter

        correctness = JSONObject()
        correctness.wrongFields = wrongFieldList
        correctness.absoluteValue = self.absoluteValue
        correctness.ratedValue = self.ratedValue
        correctness.unit = self.unit
        # 		print "correctness:", self.ratedValue, self.absoluteValue
        return (self.name, correctness)

    def getMinMaxValue(self, fieldname, data):
#         print "getMinMaxValue", fieldname#, data
#         print self.repsys.description.field[fieldname]
        if "min" in self.repsys.description.field[fieldname]:
            minValue = self.repsys.description.field[fieldname].min
            minValue = self.getValue(minValue, data)
        else:
            minValue = None
        if "max" in self.repsys.description.field[fieldname]:
            maxValue = self.repsys.description.field[fieldname].max
            maxValue = self.getValue(maxValue, data)
        else:
            maxValue = None

        return minValue, maxValue

    def getValue(self, minMaxValue, data):
        try:
            if minMaxValue.startswith('@'):
                # find out in which field value is annotated
                name = minMaxValue[1:]
                return data[name].value
            return minMaxValue
        except:
            return minMaxValue
