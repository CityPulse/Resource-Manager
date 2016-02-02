'''
Created on 5 Oct 2015

@author: thiggena
'''
import datetime

from Quality.Average.averageQuality import AverageQuality, \
    HOURLY, DAILY, WEEKLY, MONTHLY
from virtualisation.misc.jsonobject import JSONObject


class AverageQualityManager(object):
    
    def __init__(self, updateInterval):
        self.qoiMetrics = {}
        self.updateInterval = updateInterval
        self.avgTypes = [HOURLY, DAILY]
        
    def addQoIMetric(self, metric):
        self.qoiMetrics[metric.name] = AverageQuality(self.avgTypes, self.updateInterval, metric.unit)
        
    def addAvgQualityType(self, qType):
        self.avgTypes.append(qType)
        for metric in self.qoiMetrics:
            self.qoiMetrics[metric].addAvgQualityType(qType)
            
    def delAvgQualityType(self, qType):
        self.avgTypes.remove(qType)
        for metric in self.qoiMetrics:
            self.qoiMetrics[metric].delAvgQualityType(qType)
        
    def getAvgQualities(self, currentDate):
        avgQualities = JSONObject()
        for t in self.avgTypes:
            avgQualities[t] = JSONObject()
            avgQualities[t].values = []
            avgQualities[t].startDate = str(self.getStartDate(currentDate, t))
        for key in self.qoiMetrics:
            self.qoiMetrics[key].getAvgQualities(avgQualities, key)
        return avgQualities
    
    def getQualityValues(self):
        qualities = JSONObject()
        qualities.values = []
        for key in self.qoiMetrics:
            self.qoiMetrics[key].getQualityValues(qualities, key, max(self.avgTypes))
        return qualities
    
    def calculateAvgQualities(self, qoiValues):
        for entry in qoiValues:
            metric = entry
            ratedValue = qoiValues[entry].ratedValue
            absoluteValue = qoiValues[entry].absoluteValue
            self.qoiMetrics[metric].calculate(absoluteValue, ratedValue)
            
    def getValues(self, job, metricName, aTypes, avg=None, minimum=None, maximum=None):
        avgQuality = self.qoiMetrics[metricName]
        for t in aTypes:
            if t in self.avgTypes:
                job[t] = avgQuality.getValues(t, avg=avg, minimum=minimum, maximum=maximum)
            
    def getStartDate(self, currentDate, qType):
        if qType == HOURLY:
            return currentDate - datetime.timedelta(hours=1)
        elif qType == DAILY:
            return currentDate - datetime.timedelta(days=1)
        elif qType == WEEKLY:
            return currentDate - datetime.timedelta(days=7)
        elif qType == MONTHLY:
            return currentDate - datetime.timedelta(months=1)
