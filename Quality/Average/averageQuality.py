'''
Created on 5 Oct 2015

@author: thiggena
'''

from virtualisation.misc.buffer import NumericRingBuffer
from virtualisation.misc.jsonobject import JSONObject


HOURLY = "HOURLY"
DAILY = "DAILY"
WEEKLY = "WEEKLY"
MONTHLY = "MONTHLY"
avgQualityTypes = [HOURLY, DAILY, WEEKLY, MONTHLY]

def getSeconds(avgQualityType):
    if avgQualityType is HOURLY:
        return 3600;
    elif avgQualityType is DAILY:
        return 24*3600;
    elif avgQualityType is WEEKLY:
        return 7*24*3600;
    elif avgQualityType is MONTHLY:
        return 30*24*3600;

class AverageQualityObject(object):
    def __init__(self, bufferSize):
        self.absoluteBuffer = NumericRingBuffer(bufferSize)
        self.ratedBuffer = NumericRingBuffer(bufferSize)
        
    def calculate(self, absoluteValue, ratedValue):
        self.absoluteBuffer.add(absoluteValue)
        self.ratedBuffer.add(ratedValue)
    
    def getAbsoluteAverage(self):
        return self.absoluteBuffer.mean()

    def getRatedAverage(self):
        return self.ratedBuffer.mean()

    def getAbsoluteMin(self):
        return self.absoluteBuffer.min()
    
    def getAbsoluteMax(self):
        return self.absoluteBuffer.max()
    
    def getRatedMin(self):
        return self.ratedBuffer.min()
    
    def getRatedMax(self):
        return self.ratedBuffer.max()

class AverageQuality(object):
    
    def __init__(self, qTypes, updateInterval, unit):
        self.qList = {}
        self.updateInterval = updateInterval
        self.setQTypes(qTypes)
        self.unit = unit
        
    def setQTypes(self, qTypes):
        for t in qTypes:
            self.addAvgQualityType(t)
            
    def addAvgQualityType(self, qType):
        if not qType in self.qList:
            self.qList[qType] = AverageQualityObject(self.calcBufferSize(qType, self.updateInterval))
            
    def delAvgQualityType(self, qType):
        if qType in self.qList:
            del self.qList[qType]
            
    def getAvgQuality(self, qType):
        return self.qList[qType].getAverage()
    
    def getAvgQualities(self, jOb, name):
        for key in self.qList:
            q = JSONObject()
            q.absoluteValue = self.qList.get(key).getAbsoluteAverage()
            q.absoluteValueMin = self.qList.get(key).getAbsoluteMin()
            q.absoluteValueMax = self.qList.get(key).getAbsoluteMax()
            q.ratedValue = self.qList.get(key).getRatedAverage()
            q.ratedValueMin = self.qList.get(key).getRatedMin()
            q.ratedValueMax = self.qList.get(key).getRatedMax()
            q.name = name
            q.unit = self.unit
            jOb[key].values.append(q)
            
    def getQualityValues(self, jOb, name, avgQualityType):
        q = JSONObject()
        q.absoluteValues = self.qList.get(avgQualityType).absoluteBuffer.items
        q.ratedValues = self.qList.get(avgQualityType).ratedBuffer.items
        q.name = name
        q.unit = self.unit
        jOb.values.append(q)
        
    def getValues(self, t, avg=None, minimum=None, maximum=None):
        q = JSONObject()
        if avg:
            q.absoluteAvg = self.qList.get(t).getAbsoluteAverage()
            q.ratedAvg = self.qList.get(t).getRatedAverage()
        if minimum:
            q.absoluteMin = self.qList.get(t).getAbsoluteMin()
            q.ratedMin = self.qList.get(t).getRatedMin()
        if maximum:
            q.absoluteMax = self.qList.get(t).getAbsoluteMax()
            q.ratedMax = self.qList.get(t).getRatedMax()
        return q
    
    def calculate(self, absoluteValue, ratedValue):
        for key in self.qList:
            self.qList.get(key).calculate(absoluteValue, ratedValue)
            
    def calcBufferSize(self, qType, updateInterval):
        if qType == HOURLY:
            return max(3600 / updateInterval, 1)
        elif qType == DAILY:
            return max(3600 * 24 / updateInterval, 1)
        elif qType == WEEKLY:
            return max(3600 * 24 * 7 / updateInterval, 1)
        elif qType == MONTHLY:
            return max(3600 * 24 * 30 / updateInterval, 1) 