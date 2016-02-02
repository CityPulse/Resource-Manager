__author__ = 'Daniel Puschmann'


from virtualisation.aggregation.genericaggregation import GenericAggregator
from virtualisation.aggregation.dft.dftcontrol import DftControl
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log

class DftAggregator(GenericAggregator):
    def __init__(self, aggregation_configuration):
        self.dftobjects = {}

    def aggregate(self, data, sensordescription):
        result = []
        try:
            dftobjs = self.dftobjects[sensordescription.uuid]
            for f in dftobjs:
                g = dftobjs[f].control(data[f])
                if g:
                    r = JSONObject()
                    r.graph = g
                    r.sensorID = sensordescription.sensorID
                    r.propertyType = sensordescription.field[f].propertyName
                    r.category = sensordescription.sensorType
                    result.append(r)
            return result
        except KeyError:
            Log.e("Dft aggregation failed")
            return None

    def wrapper_added(self, sensordescription):
        dftobjs = {}
        for f in sensordescription.fields:
            field = sensordescription.field[f]
            if field.dataType == "int" or field.dataType == "float":
                dftobjs[f] = DftControl()
        self.dftobjects[sensordescription.uuid] = dftobjs