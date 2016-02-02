__author__ = 'Daniel Puschmann'
from virtualisation.aggregation.genericaggregation import GenericAggregator
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log
from virtualisation.aggregation.paa.paacontrol import PaaControl

class PaaAggregator(GenericAggregator):
    def __init__(self):
        self.paaobjects = {}

    def aggregate(self, data, sensordescription):
        result = []
        try:
            paaobjs = self.paaobjects[sensordescription.uuid]
            for f in paaobjs:
                g = paaobjs[f].control(data[f])
                if g:
                    r = JSONObject()
                    r.graph = g
                    r.sensorID = sensordescription.sensorID
                    r.propertyType = sensordescription.field
                    r.category = sensordescription.sensorType
                    result.append(r)
            return result
        except KeyError:
            Log.e("Paa aggregation failed")
            return None

    def wrapper_added(self, sensordescription):
        paaobjs = {}
        for f in sensordescription.fields:
            field = sensordescription.field[f]
            if field.dataType in ['int', 'float']:
                paaobjs[f] = PaaControl()
        self.paaobjects[sensordescription.uuid] = paaobjs