
import cherrypy

from virtualisation.misc.stats import Stats
from virtualisation.misc.jsonobject import JSONObject


__author__ = 'Thorben Iggena (t.iggena@hs-osnabrueck.de)'

class Stat_Api(object):
    def __init__(self, resourcemanagement):
        self.rm = resourcemanagement

    @cherrypy.expose
    def avg_processing_time(self, uuid = None, category = None):
        job = JSONObject()
        if uuid:
            uuid = uuid.split(",")
            for u in uuid:
                stats = Stats.getOrMake(u)
                job[u] = []
                pTimes = stats.getAverageProcessingTimes()
                if pTimes:
                    job[u].extend(pTimes)
                else:
                    failJob = JSONObject()
                    failJob.status = "Fail"
                    failJob.message = "UUID not found"
                    job[u] = failJob
        elif category:
            category = category.split(",")
            avgList = {}
            for c in category:
                uuidList = self.rm.getUUIDsForCategory(c)
                statList = []
                valueMap={}
                for uuid in uuidList:
                    stats = Stats.getOrMake(uuid)
                    self.test(valueMap, stats.getAverageProcessingTimes())
                    statList += stats.getAverageProcessingTimes()
                for key, value in valueMap.items():
                    valueMap[key] = value / len(uuidList)
                
                avgList[c] = []
                self.valueMapToJson(valueMap, avgList[c], None, None)
            job = JSONObject()
            for element in avgList:
                job[element] = []
                pTimes = avgList[element]
                if pTimes:
                    job[element].extend(pTimes)
                else:
                    failJob = JSONObject()
                    failJob.status = "Fail"
                    failJob.message = "Category not found"
                    job[element] = failJob
        else:
            statList = Stats.getAllStats()
            for s in statList:
                job[s.name] = []
                job[s.name].extend(s.getAverageProcessingTimes())
        return job.dumps()
    

    
    def test(self, valueMap, stats, layer=None):
        for element in stats:
            if isinstance(element, list):
                self.test(valueMap, element)
            else:
                mapname = None
                if layer:
                    mapname = layer + "." + element.name
                else:
                    mapname = element.name
                    
                if mapname in valueMap:
                    valueMap[mapname] += element.value
                else:
                    valueMap[mapname] = element.value
                
#                 print element.name, element.value, layer
                if element.values:
                    if layer:
                        self.test(valueMap, element.values, layer + "." + element.name)
                    else:
                        self.test(valueMap, element.values, element.name)
  
    def valueMapToJson(self, test, joblist, job=None, parent=None):
        if not parent:
            keys = [key for key in test if "." not in key]
        else:
            parentString = parent + "."
            keys = [key for key in test if parentString in key]
            keys = [key for key in keys if "." not in key.split(parentString)[1]]
        
        for key in keys:
            job2 = JSONObject()
            job2.name = key.split(".")[len(key.split("."))-1]
            job2.value = test[key]
    
            if job:
                if job.values:
                    job.values.append(job2)
                else:
                    job.values = []
                    job.values.append(job2)
            else:
                joblist.append(job2)
        
            test.pop(key)
            if len(test) > 0:
                self.valueMapToJson(test, joblist, job2, key)    
    
        