import datetime
from time import sleep

from virtualisation.clock.abstractclock import AbstractClock
from virtualisation.misc.log import Log


__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


class ReplayClock(AbstractClock):
    def __init__(self, speed=999, endCallback=None, endCallbackArgs=None):
        super(ReplayClock, self).__init__()
        self.delay = (1000 - speed) / 1000.0
        self.cont = True
        self.delta = datetime.timedelta(seconds=1)
        self.currentTime = None
        self.endCallback = endCallback
        self.endCallbackArgs = endCallbackArgs
        self.startDate = None
        self.endDate = None
        self.initDelay = self.delay
        
    def halfSpeed(self):
        self.delay = min(10000, max(0.001, self.delay) * 2)
        # Log.i("Queue size to high, decreasing replay clock speed")
        
    def doubleSpeed(self):
        self.delay = self.initDelay
        # Log.i("Queue size ok, switched to configured speed")

    def setTimeframe(self, startdate, enddate):
        self.startDate = startdate
        self.endDate = enddate
        self.currentTime = self.startDate

    def run(self):
        while self.cont and self.currentTime < self.endDate:
            sleep(self.delay)
            if self.wait_counter > 0:
                self.wait_event.wait()
            self.currentTime += self.delta
            self.tick()
        if self.endCallback and self.endCallbackArgs:
            self.endCallback(self.endCallbackArgs)
        elif self.endCallback:
            self.endCallback()

    def stop(self):
        self.cont = False

    def now(self):
        return self.currentTime

    def timeAsString(self):
        return self.currentTime.strftime(AbstractClock.format)

    def sleep(self, time=None):
        super(ReplayClock, self).sleep(0.5)#self.delay)
        
    def pause(self, value=1):
        self.wait_event.clear()
        with self.wait_counter_Lock:
            self.wait_counter += value
#         print "pause < wc:", self.wait_counter

    def continue_running(self):
        super(ReplayClock, self).continue_running()
