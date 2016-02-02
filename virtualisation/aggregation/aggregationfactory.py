__author__ = ['Marten Fischer (m.fischer@hs-osnabrueck.de)', 'Daniel Puschmann']

from virtualisation.aggregation.sax.saxaggregator import SaxAggregator, SaxControl
from virtualisation.aggregation.sensorsax.sensorsaxaggregator import SensorSaxAggregator, SensorSaxControl

class AggregatorFactory(object):
    entries = {"sax": SaxAggregator, "sensorsax": SensorSaxAggregator}

    @classmethod
    def make(cls, aggregator, aggregatorconfiguration):
        return AggregatorFactory.entries[aggregator](aggregatorconfiguration)
