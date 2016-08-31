__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.connection.abstractconnection import AbstractConnection

class DummyConnection(AbstractConnection):
    """
    This class fakes a connection. Can be used if no live mode is supported.
    """

    def __init__(self, wrapper):
        super(DummyConnection, self).__init__(wrapper)

    def next(self):
        return None


class StringConnection(AbstractConnection):
    """
    This class fakes a connection and returns always the same string, given in the constructor.
    """

    def __init__(self, wrapper, aString):
        super(StringConnection, self).__init__(wrapper)
        self.aString = aString

    def next(self):
        return self.aString