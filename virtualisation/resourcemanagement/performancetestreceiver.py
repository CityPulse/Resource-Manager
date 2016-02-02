import threading
from time import sleep

from virtualisation.misc.log import Log
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter
from virtualisation.wrapper.wrapperoutputreceiver import AbstractReceiver


__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class AbstractPerformanceMeter(AbstractReceiver):

    def __init__(self, delay, txt):
        self.counter = 0
        self.stop = False
        self.delay = delay
        self.txt = txt
        threading.Thread(target=self.__run).start()

    def __run(self):
        while not self.stop:
            sleep(self.delay)
            Log.i(self.counter, self.txt)
#             print self.counter, self.txt
#             print "ThreadedTriplestoreAdapter Buffer Size:", ThreadedTriplestoreAdapter.getTotalBufferSize()
            Log.i("ThreadedTriplestoreAdapter Buffer Size:", ThreadedTriplestoreAdapter.getTotalBufferSize())
            self.counter = 0

    def receive(self, parsedData, sensordescription, clock, quality):
        self.counter += 1

    def stop(self):
        self.stop = True

class PerformanceMeterSeconds(AbstractPerformanceMeter):

    def __init__(self):
        super(PerformanceMeterSeconds, self).__init__(1, "observations/s")

class PerformanceMeterMinutes(AbstractPerformanceMeter):

    def __init__(self):
        super(PerformanceMeterMinutes, self).__init__(60, "observations/min")
