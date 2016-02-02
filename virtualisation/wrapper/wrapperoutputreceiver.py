__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import abc

class AbstractReceiver(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def receive(self, parsedData, sensordescription, clock, quality):
        pass