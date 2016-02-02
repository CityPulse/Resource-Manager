__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


from reputationsystem.sink import Sink

class BlackHoleSink(Sink):
    """
    A Sink that does nothing.
    """
    def __init__(self):
        super(BlackHoleSink, self).__init__()

    def update(self, qoiMetric):
        pass

    def persist(self, observationIdList):
        pass
