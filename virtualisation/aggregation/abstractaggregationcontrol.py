__author__ = 'Daniel Puschmann'
import abc

class AbstractAggregationControl(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, aggregation_configuration):
        pass

    @abc.abstractmethod
    def control(self):
        """
        This method aggregates all
        :return:
        """
        pass