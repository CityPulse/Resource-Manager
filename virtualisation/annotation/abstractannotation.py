__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


import abc

class AbstractAnnotation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def annotateObservation(self, data, sensordescription, clock, quality):
        pass

    @abc.abstractmethod
    def annotateEvent(self,eventdata, eventdescription):
        pass