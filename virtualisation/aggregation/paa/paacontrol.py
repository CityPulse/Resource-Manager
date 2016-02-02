__author__ = 'Daniel Puschmann'

from virtualisation.misc.buffer import RingBuffer
from virtualisation.aggregation.paa.paa import Paa
import numpy as np

class PaaControl():

    def __init__(self, buffer_size=50, window_length=5):
        self.buffer = RingBuffer(buffer_size)
        self.paaobj = Paa()
        self.window_length = window_length

    def control(self, data):
        self.buffer.add(float(data.value))
        if self.buffer.fillLevel() < self.window_length:
            return None
        result = self.paaobj.paa(self.convert(data), self.window_length)

        return result


    def convert(self, data):
        return np.asarray(data)