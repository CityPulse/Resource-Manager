__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.clock.abstractclock import AbstractClock
from time import sleep
import datetime

class RealClock(AbstractClock):
    def __init__(self, endCallback=None, endCallbackArgs=None):
        super(RealClock, self).__init__()
        self.delay = 1.0
        self.cont = True
        # self.currentTime = None
        self.endCallback = endCallback
        self.endCallbackArgs = endCallbackArgs
        self.execute_jobs_async = True

    def run(self):
        while self.cont:
            sleep(self.delay)
            # self.currentTime = datetime.datetime.now()
            self.tick()
        if self.endCallback and self.endCallbackArgs:
            self.endCallback(self.endCallbackArgs)
        elif self.endCallback:
            self.endCallback()

    def stop(self):
        self.cont = False

    def now(self):
        return datetime.datetime.now()

    def timeAsString(self):
        return datetime.datetime.now().strftime(AbstractClock.format)
    
    def pause(self, value=1):
        pass

    def continue_running(self):
        pass
