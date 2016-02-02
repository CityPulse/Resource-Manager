__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


import abc
from virtualisation.wrapper.dataprovider import DataProvider

class AbstractConnection(DataProvider):
    __metaclass__ = abc.ABCMeta

    def __init__(self, wrapper):
        super(AbstractConnection, self).__init__()
        self.wrapper = wrapper

    @abc.abstractmethod
    def next(self):
        pass
