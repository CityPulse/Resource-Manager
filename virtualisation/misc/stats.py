'''
Created on 19 Oct 2015

@author: thiggena
'''
from collections import OrderedDict
import csv
import datetime
from matplotlib import pyplot

from virtualisation.misc.buffer import NumericRingBuffer
from virtualisation.misc.jsonobject import JSONObject


PATH = "./graphs/"
BUFFER_SIZE = 1000

class Element(object):
    def __init__(self, name):
        self.name = name
        
    def finish(self):
        return "Name: " + self.name  

class TimeElement(Element):
    def __init__(self, name, value=0):
        super(TimeElement, self).__init__(name)
        self.buffer = NumericRingBuffer(BUFFER_SIZE)
        [self.buffer.add(0) for _i in range(0, value)]
        self.startTime = None
        
    def started(self, test=False):
        if self.startTime:
            return True
        return False
    
    def start(self):
        if self.startTime is None:
            self.startTime = datetime.datetime.now()
        else:
            print self.name, "already started!"    
        
    def stop(self, stoptime):
        if self.startTime is not None:
            self.buffer.add((stoptime - self.startTime).total_seconds())
            self.startTime = None
        else:
            print "TimeElement", self.name, "already stopped"
        
    def finish(self):
        print super(TimeElement, self).finish()
        print "Mean:", self.mean()
        return super(TimeElement, self).finish()
        
    def mean(self):
        return self.buffer.mean()
    
    def sum(self):
        return sum(self.buffer)
    
    def getData(self, name):
        return (name, self.buffer)
    
    def insertNotUsedValue(self, values=0):
        for _i in range(0, (values-self.buffer.len())):
            self.buffer.add(0)
        
class TimeElementList(TimeElement):
    def __init__(self, name, value=0):
        super(TimeElementList, self).__init__(name, value)
        self.timeElementMap = {}
        
    def getData(self, name):
        dataList = []
        for element in self.timeElementMap:
            dataList.append(self.timeElementMap[element].getData(name + "." + element))
        dataList.append(super(TimeElementList, self).getData(name))
        return dataList
            
    def startElement(self,categoryList):
        timeElementList = None
        if categoryList[0] in self.timeElementMap:
            timeElementList = self.timeElementMap[categoryList[0]]
        else:
            timeElementList = TimeElementList(categoryList[0], self.buffer.len())
            timeElementList.start()
            self.timeElementMap[categoryList[0]] = timeElementList
        if not timeElementList.started():
            timeElementList.start()
        if len(categoryList) > 1:  
            timeElementList.startElement(categoryList[1:])

    def stopElement(self, categoryList, stoptime):
        if categoryList[0] in self.timeElementMap:
            timeElementList = self.timeElementMap[categoryList[0]]
            if len(categoryList) > 1:  
                timeElementList.stopElement(categoryList[1:], stoptime)
            else:
                if timeElementList.started():
                    timeElementList.stop(stoptime)

    def start(self):
        super(TimeElementList, self).start()

    def stop(self, stoptime):
        super(TimeElementList, self).stop(stoptime)
        [e.stop(stoptime) for e in self.timeElementMap.values() if e.started(True)]
        [e.insertNotUsedValue(self.buffer.len()) for e in self.timeElementMap.values()]
        
    def finish(self):
        super(TimeElementList, self).finish()
        for e in self.timeElementMap:
            self.timeElementMap[e].finish()
        
#     def writeCSVFile(self, name):
#         data = self.getData(self.name)
#         tuples = []
#         for e in data:
#             self.parse(e, tuples)
#         
#         csvfile = open(PATH + str(name) + "_" + str(self.name) + ".csv", 'w')
#         csvf = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         
#         header = []
#         maxEntries = 0
#         for e in tuples:
#             header.append(e[0])
#             maxEntries = max(maxEntries, e[1].len())
#         csvf.writerow(header)
#         
#         for i in range(0, maxEntries):
#             row = []
#             for e in tuples:
#                 data = e[1]
#                 if data.len() >= i+1:
#                     row.append(data.items[i])
#                 else:
#                     row.append("")
#             csvf.writerow(row)
#         csvfile.close()
    
    def parse(self, data, tuples):
        if isinstance(data, list):
            for e in data:
                self.parse(e, tuples)
        else:
            tuples.append(data)
            
    def getAverageProcessingTimes(self):
        job = JSONObject()
        job.name = self.name
        job.value = self.mean()
        if len(self.timeElementMap) > 0:
            job.values = []
        for element in self.timeElementMap:
            if len(self.timeElementMap[element].timeElementMap) > 0:
                job.values.append(self.timeElementMap[element].getAverageProcessingTimes())
            else:
                job2 = JSONObject()
                job2.name = element
                job2.value = self.timeElementMap[element].mean()   
                job.values.append(job2)
        return job

class CounterElement(Element):
    def __init__(self, name):
        super(CounterElement, self).__init__(name)
        self.counter = 0
        self.counterMap = OrderedDict()
        
    def count(self, timestamp=None):
        self.counter += 1
        if timestamp:
            self.counterMap[timestamp] = self.counter
        else:
            self.counterMap[datetime.datetime.now()] = self.counter
        
#     def writeCSVFile(self, name):
#         csvfile = open(PATH + name + "_" + self.name + "_count.csv", 'w')
#         csvf = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         header = ["date", "count"]
#         csvf.writerow(header)
#         for element in self.counterMap:
#             csvf.writerow([element, self.counterMap[element]])
#         csvfile.close()
        
class SizeElement(Element):
    def __init__(self, name):
        super(SizeElement, self).__init__(name)
        self.items = OrderedDict()
        
    def addItem(self, time, value):
        self.items[time] = value
        
    def finish(self):
        print super(SizeElement, self).finish()
        for item in self.items:
            print item, self.items[item]
            
    def plot(self, name):
        x = self.items.keys()
        y = self.items.values()
        pyplot.plot(x, y)
        print "x", x, min(x), max(x)
        print "y", y, min(y), max(y)
        pyplot.axis([min(x), max(x), min(y), max(y)])
        pyplot.savefig(PATH + name + "_" + self.name+ ".png")
        
    def getData(self, name):
        return (name, self.items)
    
#     def writeCSVFile(self, name):
#         csvfile = open(PATH + name + "_" + self.name + "_size.csv", 'w')
#         csvf = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         header = ["date", "value"]
#         csvf.writerow(header)
#         for element in self.items:
#             csvf.writerow([element, self.items[element]])
#         csvfile.close()
        
            
class Stats(object):
    instances = {}

    def __new__(cls, name):
        if name not in Stats.instances:
            Stats.instances[name] = Stats.__Stats(name)
        return Stats.instances[name]

    @classmethod
    def getOrMake(cls, name):
        if name not in Stats.instances:
            Stats.instances[name] = Stats.__Stats(name)
        return Stats.instances[name]
    
    @classmethod
    def getAllStats(cls):
        return Stats.instances.values()
    
    @classmethod
    def get(cls, name):
        if name in Stats.instances:
            return Stats.instances[name]
        return None
    
#     @classmethod
#     def writeCSVs(cls):
#         for e in Stats.instances.values():
#             e.writeCSVFiles()
   
    @classmethod
    def finish(cls):
        jobs = JSONObject()
        jobs.stats = []
        for e in Stats.instances:
            job = JSONObject()
            job.name = e
            job.value = e.getvalue()
            jobs.stats.append(job)
        return jobs
   
    class __Stats(object):

        def __init__(self, name):
            self.name = name
            self.elements = {}
            
        def finish(self):
            print "Stats for", self.name
            for e in self.elements:
                self.elements[e].finish()
        
#         def writeCSVFiles(self):
#             for e in self.elements:
#                 self.elements[e].writeCSVFile(self.name)
               
        def addSize(self, name, time, value):
            if name not in self.elements:
                element = SizeElement(name)
                self.elements[name] = element
            else:
                element = self.elements[name]
            element.addItem(time, value)

            
        def count(self, name, timestamp=None):
            if name not in self.elements:
                element = CounterElement(name)
                self.elements[name] = element
            else:
                element = self.elements[name]
            element.count(timestamp)
            
        def startMeasurement(self, categoryString):
            categories = categoryString.split(".")
            timeElementList = None
            if categories[0] in self.elements:
                timeElementList = self.elements[categories[0]]
            else:
                timeElementList = TimeElementList(categories[0])
                self.elements[categories[0]] = timeElementList
            if not timeElementList.started():
                timeElementList.start()
            if len(categories) > 1:
                timeElementList.startElement(categories[1:])
                
        def stopMeasurement(self, categoryString):
            stoptime = datetime.datetime.now()
            categories = categoryString.split(".")
            if categories[0] in self.elements:
                timeElementList = self.elements[categories[0]]
                if len(categories) > 1:
                    timeElementList.stopElement(categories[1:], stoptime)
                else:
                    if timeElementList.started():
                        timeElementList.stop(stoptime)
            else:
                print "cannot stop element", categories[0], ", related elements not stopped yet"      
                
        def getAverageProcessingTimes(self):
            times = []
            for element in self.elements:
                if isinstance(self.elements[element], TimeElementList):
                    times.append(self.elements[element].getAverageProcessingTimes())
            return times
            
        
# if __name__ == '__main__':
#     from time import sleep
#     s = Stats("test")
#     for i in range(0, 10):
#         s.startMeasurement("method")
#         s.count("testCounter")
# #         print i
# #         if i is 0:
#         s.startMeasurement("method.if")
#         sleep(0.0005)
#         s.startMeasurement("method.if.test")
#         sleep(0.0005)
#         s.stopMeasurement("method.if.test")   
#         s.stopMeasurement("method.if")   
# 
# #         else:
#         s.startMeasurement("method.else")
#         sleep(0.0005)
#         s.stopMeasurement("method.else")       
#         s.stopMeasurement("method")   
#     print s.getAverageProcessingTimes()[0].dumps()
#     print "#####" 
# 
#     s.writeCSVFiles()
