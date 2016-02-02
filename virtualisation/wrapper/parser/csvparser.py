from virtualisation.clock.abstractclock import AbstractClock

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.parser.abstractparser import AbstractParser
from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.utils import unicode2ascii as u, str2Type
import datetime as dt


class CSVParser(AbstractParser):

    def __init__(self, wrapper, names, timestampfield=None):
        """
        :param wrapper:
        :param names: Order of values as in the CSV, but must use the names as stated in the sensordescription.fields
        :param timestampfield: name of the field that contains the timestamp if it differs from the sensordescription
        :return:
        """
        super(CSVParser, self).__init__(wrapper)
        self.names = names
        self.lenNames = len(self.names)
        self.timestampcell = -1
        if timestampfield:
            self.timestampcell = self.names.index(timestampfield)
        else:
            if self.wrapper.getSensorDescription().isTimestampedStream():
                try:
                    self.timestampcell = self.names.index(self.wrapper.getSensorDescription().timestamp.inField)
                    # self.timestampformat = self.wrapper.getSensorDescription().timestamp.format
                except ValueError:
                    self.timestampcell = -1

    def parse(self, data, clock):
        if not data:  # nothing received or nothing in the history -> nothing to parse
            return None

        if self.lenNames > len(data):
            raise Exception()

        result = JOb()
        sd = self.wrapper.getSensorDescription()
        result.fields = sd.fields
        # print data
        for i in range(0, self.lenNames):
            n = self.names[i]
            if n in sd.fields:
                result[n] = JOb()
                result[n].propertyName = sd.field[n].propertyName
                result[n].propertyURI = sd.field[n].propertyURI
                if "unit" in sd.field[n]:
                    result[n].unit = sd.field[n].unit
                result[n].observationSamplingTime = clock.timeAsString()
                result[n].sensorID = sd.fullSensorID
                if self.timestampcell >= 0:
                    result[n].observationResultTime = sd.parseTimestamp(data[self.timestampcell]).strftime(AbstractClock.format)
                else:
                    result[n].observationResultTime = result[n].observationSamplingTime

                if sd.field[n].dataType == "datetime.datetime":
                    result[n].value = dt.datetime.strptime(data[i], sd.field[n].format)
                else:
                    result[n].value = str2Type(u(data[i]), sd.field[n].dataType)

        return result
