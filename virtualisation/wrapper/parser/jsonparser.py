from virtualisation.clock.abstractclock import AbstractClock

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.parser.abstractparser import AbstractParser
from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.utils import unicode2ascii as u, str2Type
import datetime as dt


class JSONParser(AbstractParser):
    """
    Maps a list of values read by a CSVReader with a given naming list
    """

    def __init__(self, wrapper):
        super(JSONParser, self).__init__(wrapper)
        self.timestampfield = None
        if self.wrapper.getSensorDescription().isTimestampedStream():
            self.timestampfield = self.wrapper.getSensorDescription().timestamp.inField
            self.timestampformat = self.wrapper.getSensorDescription().timestamp.format

    def parse(self, data, clock):
        if not data:  # nothing received or nothing in the history -> nothing to parse
            return None

        if isinstance(data, str) or isinstance(data, unicode):
            data = JOb(u(data))

        result = JOb()
        sd = self.wrapper.getSensorDescription()
        result.fields = sd.fields
        for fieldname in sd.fields:
            result[fieldname] = JOb()
            result[fieldname].propertyName = sd.field[fieldname].propertyName
            result[fieldname].propertyURI = sd.field[fieldname].propertyURI
            if "unit" in sd.field[fieldname]:
                result[fieldname].unit = sd.field[fieldname].unit
            result[fieldname].sensorID = sd.fullSensorID
            result[fieldname].observationSamplingTime = clock.timeAsString()
            if self.timestampfield and self.timestampfield in data:
                result[fieldname].observationResultTime = sd.parseTimestamp(data[self.timestampfield]).strftime(AbstractClock.format)
            else:
                result[fieldname].observationResultTime = result[fieldname].observationSamplingTime

            if sd.field[fieldname].dataType == "datetime.datetime":
                if sd.field[fieldname].format.startswith("UNIX"):
                    result[fieldname].value = sd.parseTimestamp(data[fieldname]) if fieldname in data else None
                else:
                    result[fieldname].value = dt.datetime.strptime(data[fieldname], sd.field[fieldname].format) if fieldname in data else None
            else:
                result[fieldname].value = str2Type(u(data[fieldname]), sd.field[fieldname].dataType) if fieldname in data else None

        return result
