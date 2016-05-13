import abc
from virtualisation.aggregation.sax.saxcontrol import SaxControl
from virtualisation.aggregation.dft.dftcontrol import DftControl
from virtualisation.aggregation.paa.paacontrol import PaaControl
from virtualisation.aggregation.sensorsax.sensorsaxcontrol import SensorSaxControl
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log

__author__ = ['Marten Fischer (m.fischer@hs-osnabrueck.de)', 'Daniel Puschmann']


class AggregatorControlFactory(object):
    entries = {"sax": SaxControl, 'sensorsax': SensorSaxControl, 'dft': DftControl, 'paa': PaaControl}

    @classmethod
    def make(cls, aggregator, aggregationconfiguration):
        return AggregatorControlFactory.entries[aggregator](aggregationconfiguration)

class AggregatorFactory(object):
    @classmethod
    def make(cls):
        return GenericAggregator()


class GenericAggregator(object):

    def __init__(self):
        self.aggregation_objs = {}


    def aggregate(self, data, sensordescription):
        """
        this method is called when stream data has been annotated.
        :param data:
        :param sensordescription:
        :return: The aggregated data
        """
        if not data.fields:
            return None
        result = []
        try:
            aggregation_objs = self.aggregation_objs[sensordescription.uuid]
            for key, agg in aggregation_objs.items():
                agg_result = agg.control(data[key])
                if agg_result:
                    g, start, end, size = agg_result

                    r = JSONObject()
                    r.graph = g
                    r.field = sensordescription.field[key]
                    r.sensorID = sensordescription.sensorID
                    r.propertyName = sensordescription.field[key].propertyName
                    r.category = sensordescription.sensorType
                    r.aggregationMethod = sensordescription.field[key].aggregationMethod
                    r.aggregationConfiguration = sensordescription.field[key].aggregationConfiguration
                    r.start = start
                    r.end = end
                    r.size = size
                    result.append(r)
                return result
        except Exception as e:
            Log.e("aggregation failed due to Exception", e)
            return None


    def wrapper_added(self, sensordescription):
        """
        this method is called when a new wrapper is added to the resource management component
        :param sensordescription:
        :return:
        """
        aggregation_objs = {}
        self.aggregation_objs[sensordescription.uuid] = {}

        for f in sensordescription.fields:
            field = sensordescription.field[f]
            if field.aggregationMethod:
                aggregation_method = field.aggregationMethod
                aggregation_configuration = field.aggregationConfiguration
                if field.dataType in ['int', 'float', 'long']:
                    aggregation_objs[f] = AggregatorControlFactory.make(aggregation_method, aggregation_configuration)
                self.aggregation_objs[sensordescription.uuid][f] = aggregation_objs[f]

