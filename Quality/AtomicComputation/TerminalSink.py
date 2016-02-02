__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


from reputationsystem.sink import Sink

class TerminalSink(Sink):
    def __init__(self):
        super(TerminalSink, self).__init__()
        self.metrics = []

    def update(self, qoiMetric):
        self.metrics.append(qoiMetric)

    def persist(self, observationIdList):
        print "; ".join(map(lambda x: "%s = %f" % (x.name, x.ratedValue), self.metrics))
        self.metrics = []