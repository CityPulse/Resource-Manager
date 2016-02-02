__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import abc

class AbstractParser(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, wrapper, timestampfield=None):
        self.wrapper = wrapper
        self.timestampfield = timestampfield

    @abc.abstractmethod
    def parse(self, data, clock):
        """
        gets the data from the sensor connection
        :param data: data object from sensor connection
        :param clock: the clock
        :return: received data parsed
        """
        pass