from virtualisation.clock.abstractclock import AbstractClock

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.wrapper.parser.abstractparser import AbstractParser
from virtualisation.misc.jsonobject import JSONObject as JOb
import datetime as dt


class XMLParser(AbstractParser):
    """
    Maps a list of values read by a CSVReader with a given naming list
    """

    def __init__(self, wrapper):
        super(XMLParser, self).__init__(wrapper)

        self.timestampcell = -1
        if self.wrapper.getSensorDescription().isTimestampedStream():
            try:
                self.timestampcell = -1
                self.timestampformat = self.wrapper.getSensorDescription().timestamp.format
            except ValueError:
                self.timestampcell = -1

    def parse(self, data, clock):
        raise Exception("not implemented yet!")
        if not data:  # nothing received or nothing in the history -> nothing to parse
            return None


