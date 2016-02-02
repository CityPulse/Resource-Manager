from uuid import UUID
import datetime

__author__ = "Marten Fischer (m.fischer@hs-osnabrueck.de)"

import json
import copy
from zipfile import ZipExtFile
from virtualisation.misc.utils import unicode2ascii as u
import math

class JSONObject(object):
    """Wraps a JSON object for easy access"""
    def __init__(self, obj=None):
        super(JSONObject, self).__init__()
        if obj:
            if isinstance(obj, file) or isinstance(obj, ZipExtFile):
                obj = json.load(obj, 'utf-8')
            if isinstance(obj, str):
                try:
                    obj = json.loads(obj)
                except:
                    print obj

            if isinstance(obj, dict):
                for i in obj:
                    if isinstance(obj[i], dict):
                        obj[i] = JSONObject(obj[i])
                    if isinstance(obj[i], list):
                        l = obj[i]
                        for j in range(0, len(l)):
                            if isinstance(obj[i][j], dict):
                                obj[i][j] = JSONObject(obj[i][j])

            if isinstance(obj, list):
                for i in range(0, len(obj)):
                    if isinstance(obj[i], dict) or isinstance(obj[i], list):
                        obj[i] = JSONObject(obj[i])

            self.__dict__["data"] = obj
        else:
            self.__dict__["data"] = {}

    def __getattr__(self, name):
        if not name in self.data:
            self.__dict__["data"][name] = JSONObject()
        return self.__dict__["data"][name]

    def __setattr__(self, name, value):
        self.__dict__["data"][name] = value

    def __delattr__(self, name):
        if not name in self.data:
            raise AttributeError
        del self.__dict__["data"][name]
    
    def __del__(self):
        if isinstance(self.__dict__["data"], list):
            del self.__dict__["data"]
        else:
            names = map(lambda (k,v): k, self.__dict__["data"].iteritems())
            for name in names:
                del self.__dict__["data"][name]
            del names

    def isList(self):
        return isinstance(self.__dict__["data"], list)

    def dumps(self):
        # print "dumping:", self
        d = self.__dict__["data"]
        if isinstance(d, list):
            return self.__dump_list(d)
        return self.__dump_dict(d)

    def __dump_list(self, l):
        r = []
        for i in range(0, len(l)):
            value = l[i]
            if isinstance(value, JSONObject):
                r.append(value.dumps())
            elif isinstance(value, list):
                r.append(self.__dump_list(value))
            elif isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
                value = str(value)
                r.append(json.dumps(value))
            elif isinstance(value, UUID):
                r.append(self.__encloseString(str(value)))
            elif isinstance(value, datetime.datetime):
                r.append(self.__encloseString(str(value)))
            else: #elif isinstance(value, str) or isinstance(value, unicode):
                r.append(self.__encloseString(value))
#            else:
#                r.append(value)
        return "[" + ", ".join(r) + "]"

    def __dump_dict(self, d):
        r = []
        for i in d:
            key = self.__encloseString(i)
            value = d[i]
            if isinstance(value, JSONObject):
                s = [key, value.dumps()]
            elif isinstance(value, list):
                s = [key, self.__dump_list(value)]
            elif isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
                value = str(value)
                s = [key, json.dumps(value)]
            elif isinstance(value, UUID):
                s = [key, self.__encloseString(str(value))]
            elif isinstance(value, datetime.datetime):
                s = [key, json.dumps(str(value))]
#             elif not value:
#                 s = [key, json.dumps(value)]
            else: #elif isinstance(value, str) or isinstance(value, unicode):
                s = [key, self.__encloseString(value)]
            #else:
            #    s = [key, str(value)]
            r.append(": ".join(s))
        return "{" + ", ".join(r) + "}"

    def __encloseString(self, string):
#        return '"' + str(string).replace('"', '\\\\"') + '"'
        return json.dumps(string)

    def __repr__(self):

        if isinstance(self.data, list):
            return self.data.__repr__()
        else:
            r = []
            for d in self.data:
                _d = self.data[d]
                if isinstance(_d, str) or isinstance(_d, unicode):
                    r.append(u": ".join([d, u(_d)]))
                else:
                    r.append(u": ".join([d, unicode(_d)]))
            return self.__class__.__name__ + u"<" + u", ".join(r) + u">"

    def __nonzero__(self):
        return len(self.__dict__["data"]) != 0

    def __contains__(self, item):
        return item in self.__dict__["data"]

    def __iter__(self):
        return self.__dict__["data"].__iter__()

    def __getitem__(self, key):
        return self.__dict__["data"][key]

    def __setitem__(self, key, value):
        self.__dict__["data"][key] = value

    def remove_item(self, key):
        if key in self.__dict__["data"]:
            del self.__dict__["data"][key]

    def deepcopy(self):
        return JSONObject(copy.deepcopy(self.__dict__["data"]))

    def __deepcopy__(self, memo):
        return JSONObject(copy.deepcopy(self.__dict__["data"]))

    def raw(self):
        r = self.__dict__["data"]
        if isinstance(r, list):
            ret = []
            for x in r:
                ret += [x.raw() if isinstance(x, JSONObject) else x]
            return ret
        else:
            ret = {}
            for x in r:
                ret[str(x)] = r[x].raw() if isinstance(r[x], JSONObject) else u(r[x])
                if isinstance(ret[x], unicode):
                    ret[str(x)] = u(str(ret[x]))
            return ret


if __name__ == '__main__':
    import sys
    import os
    print sys.stdout.encoding
    if sys.stdout.encoding == None:
        os.putenv("PYTHONIOENCODING",'UTF-8')
        os.execv(sys.executable,['python']+sys.argv)

    json_o = {
        "a": "test",
        "b": "xyz"
    }

    json_str = """{"status": true, "records": [{"a": 1, "b": "test", "c": {"internal": "true"}}, {"a": 2, "b": "two"}]}"""

    json_l = [ {"name": "max"}, {"name": "mustermann"}]

    # jo = JSONObject(json_o)
    # jo.c = 12
    # print jo
    # print

    jo = JSONObject(json_str)
    #print jo

    #for i in jo: print i, jo[i]

    print jo
    print "dumps"
    print jo.dumps()
    print
    print

    jo["status"] = 34
    print jo
    
    test = JSONObject()
    t = "test"
    test[t] = float("inf")
    print "test:", test
    print test.dumps()

    # del jo.records[0].c
    # print jo


    # print

    # jo = JSONObject()
    # print jo
    # if jo:
    # 	print "yes"
    # jo.test = 1
    # if jo:
    # 	print "yes2"

    # if "test" in jo:
    # 	print "yes3"

    jo = JSONObject(json_l)
    print jo
    jo[1].lastname = "Doe"
    print jo.dumps()
    print

    # field = JSONObject()
    # field.avgSpeed.propertyName="http://ict-citypulse.eu/city#AverageSpeed"
    # field.avgSpeed.unit="http://ict-citypulse.eu/city:km-per-hour"
    # field.vehicleCount.propertyName="http://ict-citypulse.eu/city#VehicleCount"
    # field.vehicleCount.unit="http://muo.net/Number"

    # print field
    # print "dumps"
    # print field.dumps()
    # print

    sensordescription = JSONObject()
    sensordescription.sensorName = "aarhus_road_traffic_158466"
    sensordescription.source = "http://ckan.projects.cavi.dk/api/action/datastore_search?resource_id=d7e6c54f-dc2a-4fae-9f2a-b036c804837d"
    sensordescription.author = "cityofaarhus" #or id of user profile
    sensordescription.sensorType = "Aarhus_Road_Traffic" #serviceCategory
    sensordescription.sourceType = "pull_http"
    sensordescription.sourceFormat = "application/csv" #MIMEs
    sensordescription.information = "Road traffic for the City of Aarhus"
    sensordescription.sensorID = 158466 #or http://ckan.projects.cavi.dk/api/action/datastore_search?resource_id=d7e6c54f-dc2a-4fae-9f2a-b036c804837d#158466"
    sensordescription.uuid = "ed478823-9264-44db-83f1-113f83c21326" #platform internal unique id
    sensordescription.location = "POINT(10.56 50.52)" #or "LINESTRING(10.52 50.2234, 10.534 50.323)"
    sensordescription.movementBuffer = "3m" # in meter, 0 means steationary
    sensordescription.updateInterval = "15mins" #with push an interval to send a keep alive message
    sensordescription.fields = "avgMeasuredTime, medianMeasuredTime, avgSpeed, vehicleCount, _id, REPORT_ID, timestamp".split(", ")
    sensordescription.field.avgSpeed.propertyName = "http://ict-citypulse.eu/city#AverageSpeed"
    sensordescription.field.avgSpeed.unit = "http://ict-citypulse.eu/city:km-per-hour"
    sensordescription.field.vehicleCount.propertyName = "http://ict-citypulse.eu/city#VehicleCount"
    sensordescription.field.vehicleCount.unit = "http://muo.net/Number"

    sensordescription2 = sensordescription.deepcopy()
    sensordescription2.sensorID = 192854
    sensordescription2.sensorName = "aarhus_road_traffic_192854"


    print sensordescription.dumps()
    print
    print sensordescription2.dumps()

    f = open("../../wrapper_dev/aarhus_traffic/aarhus-traffic-points.json", "r")
    jo = JSONObject(f)
    print jo.result.records[0].REPORT_ID
