__author__ = ['Marten Fischer (m.fischer@hs-osnabrueck.de)', 'Daniel Puschmann']

from virtualisation.aggregation.genericaggregation import GenericAggregator
from virtualisation.aggregation.sax.saxcontrol import SaxControl
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log

class SaxAggregator(GenericAggregator):
    def __init__(self):
        self.aggregation_objs = {}

    def aggregate(self, data, sensordescription):
        if not data.fields:
            # Log.e("There was no data available so it could not be aggregated")
            return None
        result = []
        try:
            saxobjs = self.aggregation_objs[sensordescription.uuid]
            for f in saxobjs:
                g = saxobjs[f].control(data[f])
                if g:
                    r = JSONObject()
                    r.graph = g
                    r.sensorID = sensordescription.sensorID
                    r.propertyType = sensordescription.field[f].propertyName
                    r.category = sensordescription.sensorType
                    result.append(r)
            del data
            if result is not None and len(result) is not 0:
                Log.d2('SaxAggregator: Aggregation successful %s' % str(result))
            return result
        except Exception as e:
            Log.e("aggregation failed due to Exception", e)
            return None
