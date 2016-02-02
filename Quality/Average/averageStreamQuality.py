'''
Created on 22 Oct 2015

@author: thiggena
'''
from Quality.Average.averageQuality import HOURLY, \
    getSeconds
import saopy
from virtualisation.annotation.staticannotation import StaticAnnotator
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter


class AverageStreamQuality(object):
    '''
    classdocs
    '''


    def __init__(self, resourcemanagement, clock):
        self.updateInterval = HOURLY
        self.rm = resourcemanagement
        self.clock = None
        self.jobID = None
        self.setClock(clock)
#         self.qoiList = "Age", "Completeness", "Correctness", "Frequency", "Latency"
        self.qoiList = None
        
    def setClock(self, clock):
        self.delClockJob()
        self.clock = clock
        self.addClockJob()

    def addClockJob(self):
        self.jobID = self.clock.addJob(getSeconds(self.updateInterval), self.updateAverageQuality, args=(), reoccurring=True)
    
    def delClockJob(self):
        if self.jobID:
            self.clock.removeJob(self.jobID)
        self.jobID = None
    
    def updateAverageQuality(self):
        job = self.getAvgQualities()
        graphs = self.createGraph(job)
        #save graph
        if self.rm.args.triplestore:
            ThreadedTriplestoreAdapter.getOrMake("citypulse/avgquality").deleteGraph("citypulse/avgquality")
            for graph in graphs:
                ThreadedTriplestoreAdapter.getOrMake( "citypulse/avgquality").addGraph(graph)
        
    def getAvgQualities(self):
        from virtualisation.wrapper.abstractwrapper import AbstractWrapper, AbstractComposedWrapper
        uuid = []
        wrappers = self.rm.wrappers
        for wrapper in wrappers:
            if isinstance(wrapper, AbstractWrapper):
                uuid.append(wrapper.getSensorDescription().uuid)
            elif isinstance(wrapper, AbstractComposedWrapper):
                for aWrapper in wrapper.wrappers:
                    uuid.append(aWrapper.getSensorDescription().uuid)
        qualities = []
        for _uuid in uuid:
            wrapper = self.rm.getWrapperByUUID(_uuid)
            if wrapper:
                if wrapper.qoiSystem.initialised:
                    if not self.qoiList:
                        self.qoiList = [m.name for m in wrapper.qoiSystem.reputationSystem.metrics]
                    avgQualities = []
                    avgQualities.append(wrapper.qoiSystem.getLastQoI([self.updateInterval], avg=True, minimum=True, maximum=True))
                    avgQualities[-1].uuid = wrapper.getSensorDescription().uuid
                    avgQualities[-1].eventProfile = wrapper.getSensorDescription().namespace + "EventProfile-" + _uuid
                    qualities.extend(JSONObject(avgQualities))
        return qualities
        
    def createGraph(self, jobList):
        graphList = []
        for element in jobList:
            saoOut = saopy.SaoInfo()
            eventprofile = saopy.ces.EventProfile(element.eventProfile)
            saoOut.add(eventprofile)
            for qoiName in self.qoiList:
                quality = None
                quality = getattr(saopy.qoi, qoiName)("http://ict-citypulse.eu/city#hourly-avg%s-%s" % (qoiName, element.uuid))
                
                tmp = element[qoiName][self.updateInterval].ratedAvg
                if tmp:
                    setattr(quality, "hasRatedQuality", "%.3f" % float(tmp))
                else:
                    setattr(quality, "hasRatedQuality", "%s" % tmp)
                    
                tmp = element[qoiName][self.updateInterval].absoluteAvg
                if tmp:
                    setattr(quality, "hasAbsoluteQuality", "%.3f" % float(tmp))
                else:
                    setattr(quality, "hasAbsoluteQuality", "%s" % tmp)

                setattr(quality, "hasUnitOfMeasurement", saopy.muo.UnitOfMeasurement("%s" % element[qoiName].unit))
                eventprofile.hasQuality.add(quality)
                saoOut.add(quality)
            
            graph = saopy.RDFInterface.exportRDFGraph(saoOut)
#             print graph.serialize(format="n3")
            graphList.append(graph)
        return graphList

if __name__ == '__main__':
    test = JSONObject("""[{"Latency": {"CURRENT": {"ratedValue": 1.0, "absoluteValue": 0.000349}, "HOURLY": {"absoluteAvg": 0.000798733333333333, "ratedMax": 0.001507, "ratedAvg": 1.0, "absoluteMin": 0.000347, "absoluteMax": 0.001507, "ratedMin": 0.000347}, "unit": "http://purl.oclc.org/NET/muo/ucum/unit/time/second"}, "Completeness": {"CURRENT": {"ratedValue": 1.0, "absoluteValue": 2}, "HOURLY": {"absoluteAvg": 2.0, "ratedMax": 2, "ratedAvg": 1.0, "absoluteMin": 2, "absoluteMax": 2, "ratedMin": 2}, "unit": "http://purl.oclc.org/NET/muo/ucum/physical-quality/number"}, "eventProfile": "http://test.de/EventProfile-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f", "uuid": "4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f", "Age": {"CURRENT": {"ratedValue": 1.0, "absoluteValue": 0.0}, "HOURLY": {"absoluteAvg": 0.0, "ratedMax": 0.0, "ratedAvg": 1.0, "absoluteMin": 0.0, "absoluteMax": 0.0, "ratedMin": 0.0}, "unit": "http://purl.oclc.org/NET/muo/ucum/unit/time/second"}, "Correctness": {"CURRENT": {"ratedValue": 1.0, "absoluteValue": 1}, "HOURLY": {"absoluteAvg": 1.0, "ratedMax": 1, "ratedAvg": 1.0, "absoluteMin": 1, "absoluteMax": 1, "ratedMin": 1}, "unit": "http://purl.oclc.org/NET/muo/ucum/unit/fraction/percent"}, "Frequency": {"CURRENT": {"ratedValue": 0.6052631578947429, "absoluteValue": 0.01694915254237288}, "HOURLY": {"absoluteAvg": "inf", "ratedMax": "inf", "ratedAvg": 0.559912280701759, "absoluteMin": 0.015873015873015872, "absoluteMax": "inf", "ratedMin": 0.015873015873015872}, "unit": "http://purl.oclc.org/NET/muo/ucum/unit/frequency/Herz"}}]""")
    print type(test)
    print test.dumps()
    a = AverageStreamQuality(None, None)
    a.createGraph(test)
    
    
    
    pass