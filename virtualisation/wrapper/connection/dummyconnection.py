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
