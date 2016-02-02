__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import threading

class TimeStampedItem(object):
    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.data = data

class TimestampedList(object):
    def __init__(self):
        self.items = []

    def add(self, timestamp, data):
        self.items.append(TimeStampedItem(timestamp, data))

    def sort(self):
        """
        Sort the list based on the given timestamps
        :return: nothing
        """
        self.items.sort(key=lambda x: x.timestamp)

    def next(self, timestamp):
        """
        All items before the returned one are deleted.
        :param timestamp: A timestamp as datetime object as the maximum threshold.
        :return: Returns the item closest and smaller to the given timestamp (<=). In other words: 'the item must already have happend'. If no item has happend before the given timestamp None is returned.
        """
        i = -1
        for x in range(0, len(self.items)):
            if self.items[x].timestamp <= timestamp:
                i = x
            else:
                # self.items[0:i] = []
                del self.items[0:i]
                return self.items.pop(0).data
        return None

class BufferedTimestampedList(object):
    def __init__(self, bufferLength, fillFunction, fillBelow):
        """

        :param bufferLength: how many items to buffer
        :param fillFunction: a one argumented function to refill the buffer. The argument is this instant of the list. When the buffer is refilled the functon must call fillFunctionComplete().
        :param fillBelow: call the fillFunction if less items are available
        :return:
        """
        self.items = []
        self.itemsLock = threading.Lock()
        self.bufferLength = bufferLength
        self.fillFunction = fillFunction
        self.fillBelow = fillBelow
        self.currentItem = 0
        self.loaderThread = None

        self.checkFillLevel(sync=True)

    def add(self, timestamp, data):
        self.items.append(TimeStampedItem(timestamp, data))

    def _sort(self):
        """
        Sort the list based on the given timestamps
        :return: nothing
        """
        self.items.sort(key=lambda x: x.timestamp)

    def next(self, timestamp):
        """
        All items before the returned one are deleted.
        :param timestamp: A timestamp as datetime object as the maximum threshold.
        :return: Returns the item closest and smaller to the given timestamp (<=). In other words: 'the item must already have happend'. If no item has happend before the given timestamp None is returned.
        """
        if len(self.items) > 0 and self.items[0].timestamp > timestamp:
            return None
        
        i = -1
        self.checkFillLevel()
        # print len(self.items), self.items[0].timestamp, self.items[-1].timestamp, timestamp
        if len(self.items) > 0 and self.items[-1].timestamp < timestamp:
            # at this point no item satisfies the timestamp. Dump all and reload.
            self.items = []
            self.checkFillLevel()
        self.itemsLock.acquire()
        for x in range(0, len(self.items)):
            # print self.items[x].timestamp, "and", timestamp
            if self.items[x].timestamp <= timestamp:
                i = x
            elif i >= 0:
#                 self.items[0:i] = []
                del self.items[0:i]
                # print "next will be", self.items[0].timestamp
                try:
                    self.itemsLock.release()
                    return self.items.pop(0).data
                except IndexError:
                    self.itemsLock.release()
                    return None
        self.itemsLock.release()
        return None

    def checkFillLevel(self, offset=0, sync=False):
        if not self.loaderThread and self.fillFunction and len(self.items) - offset < self.fillBelow:
            if sync:
                self.itemsLock.acquire()
                self.fillFunction(self)
            else:
                self.loaderThread = threading.Thread(target=self.fillFunction, args=(self,))
                self.itemsLock.acquire()
                self.loaderThread.start()

    def fillFunctionComplete(self):
        self.loaderThread = None
        self._sort()
        self.itemsLock.release()

    def stopFillFunction(self):
        self.fillFunction = None

    def scrollTo(self, startdate):
        x = 0
        while x < len(self.items) and self.items[x].timestamp < startdate:
            x += 1
            if len(self.items) - x < self.fillBelow and self.fillFunction:
                self.itemsLock.acquire()
                self.fillFunction(self)

        self.items[0:x] = []
        return len(self.items) > 0
