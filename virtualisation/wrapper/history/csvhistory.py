import traceback
__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.history.abstractreader import AbstractReader
from virtualisation.misc.buffer import Buffer
from virtualisation.misc.lists import TimestampedList, BufferedTimestampedList
from virtualisation.misc.log import Log
import csv
import os.path

class CSVHistoryReader(AbstractReader):
    def __init__(self, wrapper, filehandle, firstLineHeader=True, headers=None, delimiter=',', timestampfield=None):
        # if not os.path.exists(filename):
        #     raise Exception("Historic data for" + str(self) + "not available")
        super(CSVHistoryReader, self).__init__(wrapper, timestampfield)
        try:
            self.filehandle = filehandle
            self.reader = csv.reader(self.filehandle, delimiter=delimiter)
            if firstLineHeader:
                self.headers = self.reader.next()
            if headers:
                self.headers = headers

            # read and sort the data
            sd = self.wrapper.getSensorDescription()
            tsdata = timestampfield
            if not tsdata and sd.isTimestampedStream():
                tsdata = sd.timestamp.inField
            if tsdata:
                self.__loadtimestamped(tsdata)
            else:
                self.__loadnormal()
        except IOError as error:
            raise error

    def __loadtimestamped(self, tsdata):
        try:
            self.timestampindex = self.headers.index(tsdata)
            self.data = BufferedTimestampedList(200, self.fillBuffer, 20)
        except ValueError as e:
            self.__loadnormal()

    def __loadnormal(self):
        self.data = []
        for row in self.reader:
            self.data.append(row)

    def fillBuffer(self, aList):
        sd = self.wrapper.getSensorDescription()
        for x in range(0, aList.bufferLength):
            try:
                row = self.reader.next()
                ts = sd.parseTimestamp(row[self.timestampindex])
                aList.add(ts, row)
            except StopIteration:
                # print sd.sensorID, "no more data"
                aList.stopFillFunction()
                break
        aList.fillFunctionComplete()

    def tick(self, clock):
        if isinstance(self.data, list):
            return self.data.pop(0) if len(self.data) > 0 else None
        else:
#             clock.pause()
            x = self.data.next(clock.now())
#             clock.continue_running()
            return x
        
    def setTimeframe(self, startdate, enddate):
        if not isinstance(self.data, list):
            Log.i("Searching start date in historic data for", self.wrapper.getSensorDescription().sensorID, "...")
            if self.data.scrollTo(startdate):
                Log.i("done")
            else:
                Log.w("no historic data beginning at", startdate, "found")
        super(CSVHistoryReader, self).setTimeframe(startdate, enddate)

# class CSVHistoryReader(AbstractReader):
#     def __init__(self, wrapper, filename, firstLineHeader=True, headers=[]):
#         super(CSVHistoryReader, self).__init__(wrapper)
#         try:
#             self.filehandle = open(filename, "rb")
#             r = csv.reader(self.filehandle, delimiter=',')
#             self.headers = headers
#             if firstLineHeader:
#                 self.headers = r.next()
#
#             # read and sort the data
#             sd = self.wrapper.getSensorDescription()
#             if sd.isTimestampedStream():
#                 self.__loadtimestamped(r, sd)
#             else:
#                 self.__loadnormal(r)
#         except IOError as error:
#             print "Historic data for", self, "not available"
#             print error
#             raise error
#
#     def __loadtimestamped(self, reader, sd):
#         self.data = TimestampedList()
#         try:
#             i = self.headers.index(sd.timestamp.inField)
#             for row in reader:
#                 ts = sd.parseTimestamp(row[self.timestampindex])
#                 self.data.add(ts, row)
#             self.data.sort()
#         except ValueError:
#             self.__loadnormal(reader)
#
#     def __loadnormal(self, reader):
#         self.data = []
#         for row in reader:
#             self.data.append(row)
#
#     def tick(self, clock):
#         if isinstance(self.data, list):
#             return self.data.pop(0)
#         else:
#             return self.data.next(clock.now())


# class CSVHistoryReader(AbstractReader):
#     def __init__(self, wrapper, filename, firstLineHeader=True, headers=[], bufferLength=20):
#         super(CSVHistoryReader, self).__init__(wrapper)
#         self.buffer = Buffer(bufferLength, fillBelow=3, fillFunction=self.fillBuffer)
#         try:
#             self.filehandle = open(filename, "rb")
#             self.r = csv.reader(self.filehandle, delimiter=',')
#             self.headers = headers
#             if firstLineHeader:
#                 self.headers = self.r.next()
#             self.fillBuffer()
#         except IOError as error:
#             print "Historic data for", self, "not available"
#             print error
#             raise error
#
#     def fillBuffer(self):
#         tmp = []
#         for i in range(0, self.buffer.length):
#             tmp.append(self.r.next())
#         self.buffer.append(tmp)
#
#     def tick(self):
#         return self.buffer.pick()
#
#     def setTimeframe(self, startdate, enddate):
#         super(CSVHistoryReader, self).setTimeframe(startdate, enddate)
#         sd = self.wrapper.getSensorDescription()
#         if "timestamp" in sd:
#             # foreward to the timestamp after the startdate
#             tsAfter = startdate + datetime.timedelta(seconds=sd.updateInterval)
#             # find the position of the timestamp
#             i = -1
#             for x in range(0, len(self.headers)):
#                 if self.headers[x] == sd.timestamp.inField:
#                     i = x
#                     break
#             if i < 0:
#                 return
#             while self.buffer.size():
#                 data = self.buffer.peek()
#                 ts = datetime.datetime.strptime(data[i], sd.timestamp.format)
#                 if ts >= tsAfter:
#                     break
#                 else:
#                     self.buffer.pick()
#



