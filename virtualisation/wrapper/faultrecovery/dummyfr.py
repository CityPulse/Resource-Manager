__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


class FaultRecovery:

    def __init__(self):
        self.counter = 0

    def addValidMeasurement(self, measurement):
        # print "valid measurement", measurement, "added.'"
        self.counter += 1
        pass

    def reportInvalidMeasurement(self):
        # print "invalid measurement reported"
        pass

    def isReady(self):
        return self.counter >= 20

    def getEstimation(self):
        return -1