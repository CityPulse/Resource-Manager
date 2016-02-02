__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import abc
from virtualisation.wrapper.dataprovider import DataProvider

class AbstractReader(DataProvider):

    __metaclass__ = abc.ABCMeta

    def __init__(self, wrapper, timestampfield=None):
        super(AbstractReader, self).__init__()
        self.wrapper = wrapper
        self.timestampfield = timestampfield
        self.startdate = None
        self.enddate = None

    @abc.abstractmethod
    def tick(self, clock):
        pass

    def setTimeframe(self, startdate, enddate):
        self.startdate = startdate
        self.enddate = enddate