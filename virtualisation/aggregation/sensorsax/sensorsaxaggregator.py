__author__ = ['Marten Fischer (m.fischer@hs-osnabrueck.de)', 'Daniel Puschmann']

from virtualisation.aggregation.genericaggregation import GenericAggregator
from virtualisation.aggregation.sensorsax.sensorsaxcontrol import  SensorSaxControl
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log
from datetime import timedelta

class SensorSaxAggregator(GenericAggregator):
    def __init__(self, aggregation_configuration):
        self.sensorsaxobjects = {}
        self.config = aggregation_configuration.sensorsax

    def aggregate(self, data, sensordescription):
        if not data.fields:
            # Log.e("There was no data available so it could not be aggregated")
            return None
        result = []
        try:
            # print "data is", data, self.saxobjects[sensordescription.uuid]
            sensorsaxobjs = self.sensorsaxobjects[sensordescription.uuid]
            for f in sensorsaxobjs:
                g = sensorsaxobjs[f].control(data[f])
                if g:
                    r = JSONObject()
                    r.graph = g
                    r.sensorID = sensordescription.sensorID
                    r.propertyType = sensordescription.field[f].propertyName
                    r.category = sensordescription.sensorType
                    result.append(r)
            del data
            if result is not None and len(result) is not 0:
                Log.d2('Aggregation successful %s' % str(result))
            return result
        except Exception as e:
            Log.e("aggregation failed due to Exception", e)
            return None

    def wrapper_added(self, sensordescription):
        saxobjs = {}
        for f in sensordescription.fields:
            field = sensordescription.field[f]
            if field.dataType == "int" or field.dataType == "float" or field.dataType == "long":
                if self.config.unit_of_window == 'hours':
                    min_window = timedelta(hours=self.config.minimum_window_length)
                    max_window = timedelta(hours=self.config.maximum_window_length)
                elif self.config.unit_of_window == 'minutes':
                    min_window = timedelta(minutes=self.config.minimum_window_length)
                    max_window = timedelta(minutes=self.config.maximum_window_length)
                elif self.config.unit_of_window == 'days':
                    min_window = timedelta(days=self.config.minimum_window_length)
                    max_window = timedelta(days=self.config.maximum_window_length)
                else:
                    Log.e('Unit of time window is not supported: %s' % self.config.unit_of_window)
                saxobjs[f] = SensorSaxControl(min_window, max_window, self.config.sensitvity_level,
                                              self.config.alphabet_size, self.config.word_length)
        self.sensorsaxobjects[sensordescription.uuid] = saxobjs
