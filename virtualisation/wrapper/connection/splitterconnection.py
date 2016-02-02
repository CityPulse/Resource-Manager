__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import abstractconnection

class SplitterConnection(abstractconnection.AbstractConnection):
    """
    This connection is simply to make the connection of an 'internal' wrapper and the splitter component of a ComposedWrappper
    """

    def __init__(self, wrapper, composedWrapper):
        super(SplitterConnection, self).__init__(wrapper)
        self.sensorDescription = wrapper.getSensorDescription()
        self.composedWrapper = composedWrapper

    def next(self):
        return self.composedWrapper.splitter.next(self.sensorDescription)
