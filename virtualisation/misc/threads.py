import threading
import Queue
from time import sleep
from virtualisation.misc.log import Log as L

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()


class QueueThread(StoppableThread):
#     def __init__(self, maxsize=100, handler=None, timeout=0.1):
    def __init__(self, handler=None, timeout=0.01):
        """

        :param maxsize: the maximum number of items in the queue
        :param handler: A 1 argument function, which is called asynchronously when an item in the queue is available.
            The argument for the function is a queue item added before.
        :param timeout: Float number how much delay (in seconds) between checks if an item in the queue is ready.
        :return:
        """
        super(QueueThread, self).__init__()
#         self.queue = Queue.Queue(maxsize)
        self.queue = Queue.Queue()
        self.handler = handler
        self.timeout = timeout


    def add(self, item):
        if self.queue.full():
            L.d2("trying to add something into a full queue:", item)
        self.queue.put(item, True)
        L.d2("QueueThread size:", self.queue.qsize())


    def run(self):
        if not self.handler:
            raise Exception("No handler set!")
        while True:
            sleep(self.timeout)
            if not self.stopped():
                while not self.queue.empty():
                    self.handler(self.queue.get())
                    self.queue.task_done()
            else:
                break
            
    def getQueueSize(self):
        return self.queue.qsize()

