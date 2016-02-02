__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


import abc

class AbstractSplitter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, wrapper):
        self.wrapper = wrapper

    @abc.abstractmethod
    def next(self, sensorDescription):
        pass

    @abc.abstractmethod
    def update(self, data):
        """
        This method is call when the connection of the ComposedWrapper is updated
        :param data: The data received by the ComposedWrapper's connection
        :return:
        """
        pass