from threading import Thread

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class Buffer():
    def __init__(self, length, initialValues=[], fillFunction=None, fillBelow=10):
        self.length = length
        self.items = initialValues
        self.fillFunction = fillFunction
        self.fillBelow = fillBelow
        self.loaderThread = None

    def pick(self):
        if not self.loaderThread and self.fillFunction and len(self.items) <= self.fillBelow:
            # self.fillFunction()
            self.loaderThread = Thread(target=self.fillFunction)
            self.loaderThread.start()
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return None

    def append(self, items):
        self.items[len(self.items):] = items
        self.loaderThread = None

    def peek(self):
        return self.items[0]

    def size(self):
        """
        :return: number of items currently in the buffer
        """
        return len(self.items)
        

class RingBuffer(object):
    """docstring for RingBuffer"""
    def __init__(self, size):
        self.size = size
        self.items = []

    def add(self, item):
        self.items.append(item)
        if len(self.items) > self.size:
            del self.items[0]

    def min(self):
        _items = filter(lambda x: x is not None, self.items)
        return min(_items) if len(_items) > 0 else float('nan')

    def max(self):
        _items = filter(lambda x: x is not None, self.items)
        return max(_items) if len(_items) > 0 else float('nan')

    def fillLevel(self):
        return len(self.items)

    def len(self):
        return self.fillLevel()

    def __iter__(self):
        return self.items.__iter__()
    
    def isFull(self):
        return self.size <= self.len()

class NumericRingBuffer(RingBuffer):
    """docstring for NumericRingBuffer"""
    def __init__(self, size):
        super(NumericRingBuffer, self).__init__(size)
        self.counter = 0
        self.sum = 0.0

    def add(self, item):
        super(NumericRingBuffer, self).add(item)
        self.counter += 1
        self.sum += item

    def mean(self):
        return float('nan') if self.fillLevel() == 0 else float(sum(self.items)) / self.fillLevel()

    def mean_all(self):
        return self.sum / self.counter
