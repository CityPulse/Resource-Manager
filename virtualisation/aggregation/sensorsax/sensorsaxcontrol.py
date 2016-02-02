from datetime import datetime

__author__ = ['sefki', 'Marten Fischer (m.fischer@hs-osnabrueck.de)', 'Daniel Puschmann']

from virtualisation.aggregation.sax.sax import Sax
import numpy as np
from virtualisation.aggregation.abstractaggregationcontrol import AbstractAggregationControl


class SensorSaxControl(AbstractAggregationControl):
    def __init__(self, minimum_window_length, maximum_window_length, sensitivity_level, alphabet_size, word_length):
        self.buffer = []
        self.saxobj = Sax(alphabet_size)
        self.minimum_window_length = minimum_window_length
        self.maximum_window_length = maximum_window_length
        self.sensitivity_level = sensitivity_level
        self.word_length = word_length

    def control(self, data):
        if len(self.buffer) is 0:
            """
            In this case we start a new SAX pattern, so we save the time_stamp
            """
            self.start_time = datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S')
        current_time = datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S')
        self.buffer.append(float(data.value))
        if self.start_time + self.minimum_window_length < current_time:
            """
            Our minimum time window has not been reached yet, keep buffering data
            """
            return None
        if self.start_time + self.maximum_window_length > current_time or np.std(self.buffer) > self.sensitivity_level:
            """
            Either we have reached the maximum window size or we have enough variation in the data to warrant aggregation
            """
            result = self.saxobj.sax(self.filterConvert(self.buffer), self.word_length)
            self.buffer = []
            self.start_time = datetime.strptime(data.observationResultTime, '%Y-%m-%dT%H:%M:%S')
            return result[0]
        else:
            """
            The standard variation does not go over sensitivity level threshold, so we keep buffering data
            """
            return None


    def filterConvert(self, aList):
        # aList = filter(None, aList)
        aList = np.asarray(aList)
        return aList
