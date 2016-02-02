import abc
import datetime
import threading
from time import sleep
import uuid

from virtualisation.misc.log import Log


__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


class ClockEntry(object):
    def __init__(self, secondsDelay, uuid, reoccurring=True):
        self.secondsDelay = secondsDelay
        self.reoccurring = reoccurring
        self.ticks = secondsDelay
        self.uuid = uuid

    def tick(self):
        self.ticks -= 1
#         print "Tick:", self.ticks
#         Log.d2("ClockEntry tick", self.ticks)
        r = self.ticks == 0
        if r and self.reoccurring:
            self.ticks = self.secondsDelay
        return r

    def reset(self):
        self.ticks = self.secondsDelay

    def do(self):
        pass


class Notification(ClockEntry):
    def __init__(self, secondsDelay, uuid, event, reoccurring=True):
        super(Notification, self).__init__(secondsDelay, uuid, reoccurring)
        self.event = event

    def do(self):
        while self.event.isSet():
            pass
        self.event.set()


class Job(ClockEntry):
    def __init__(self, secondsDelay, uuid, function, args=(), reoccurring=True):
        super(Job, self).__init__(secondsDelay, uuid, reoccurring)
        self.function = function
        self.args = args

    def do(self):
        if self.args is not ():
            self.function(self.args)
        else:
            self.function()


class AbstractClock(object):
    __metaclass__ = abc.ABCMeta

    format = "%Y-%m-%dT%H:%M:%S%z"
    parserformat = "%Y-%m-%dT%H:%M:%S"

    secondsInADay = 60*30 #86400

    def __init__(self):
        self.jobs = {}
        self.notifications = {}
        self.lock = threading.Lock()
        self.filtermethod = lambda (k, v): v.tick()
        self.removefiltermethod = lambda (k, v): v.reoccurring is False and v.ticks <= 0
        self.wait_counter_Lock = threading.Lock()
        self.wait_counter = 0
        self.wait_event = threading.Event()
        self.dayPrintCounter = AbstractClock.secondsInADay # used to print the time once a 'day'
        self.execute_jobs_async = False

    def addNotification(self, secondsDelay, condition, reoccurring=True):
        self.lock.acquire()
        _id = uuid.uuid4()
        self.notifications[_id] = Notification(secondsDelay, _id, condition, reoccurring)
        self.lock.release()
        return _id

    def removeNotification(self, _id):
        del self.notifications[_id]

    def removeJob(self, _id):
        del self.jobs[_id]

    def resetJob(self, _id):
        self.jobs[_id].reseet()

    def resetNotification(self, _id):
        self.notifications[_id].reset()

    def addJob(self, secondsDelay, function, args=(), reoccurring=True):
        self.lock.acquire()
        _id = uuid.uuid4()
        self.jobs[_id] = Job(secondsDelay, _id, function, args, reoccurring)
        self.lock.release()
        return _id

    def tick(self):
#         Log.d2("AbstractClock tick")
        self.dayPrintCounter -= 1
        if self.dayPrintCounter == 0:
            self.dayPrintCounter = AbstractClock.secondsInADay
            Log.i("It is", self.now())
            print "It is", self.now()

#         Log.d2("AbstractClock notification handling")
        notifications = filter(self.filtermethod, self.notifications.copy().iteritems())
        self.pause(len(notifications))
        for k, v in notifications:
            v.do()
        del notifications
#         Log.d2("AbstractClock notification handling finished")
#         Log.d2("AbstractClock job")
        jobs = filter(self.filtermethod, self.jobs.copy().iteritems())
        for k, v in jobs:
            if self.execute_jobs_async:
                threading.Thread(target=v.do).start()
            else:
                v.do()
        del jobs
#         Log.d2("AbstractClock job handling finished")

#         Log.d2("AbstractClock delete self.notifications/jobs")
        self.lock.acquire()
        notifications = filter(self.removefiltermethod, self.notifications.copy().iteritems())
        for k, v in notifications:
            del self.notifications[k]
        jobs = filter(self.removefiltermethod, self.jobs.copy().iteritems())
        for k, v in jobs:
            if k in self.jobs:
                del self.jobs[k]
#         Log.d2("AbstractClock delete finished")    
        
        # tmp = filter(self.removefiltermethod, self.notifications.copy().iteritems())
        # del self.notifications
        # self.notifications = tmp
        # tmp = filter(self.removefiltermethod, self.jobs.copy().iteritems())
        # del self.jobs
        # self.jobs = tmp
        self.lock.release()

    def runAsync(self):
        threading.Thread(target=self.run).start()

    @abc.abstractmethod
    def pause(self, value=1):
        pass

    @abc.abstractmethod
    def continue_running(self):
        with self.wait_counter_Lock:
            self.wait_counter -= 1
    #         print "> wc:", self.wait_counter
            if self.wait_counter <= 0:
                self.wait_event.set()


    def sleep(self, time=None):
        if time:
            sleep(time)

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def now(self):
        pass
    
    def halfSpeed(self):
        pass
        
    def doubleSpeed(self):
        pass

    @abc.abstractmethod
    def timeAsString(self):
        return datetime.strftime(AbstractClock.format)
