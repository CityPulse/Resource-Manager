__author__ = 'Daniel Puschmann'

from virtualisation.misc.buffer import RingBuffer
from virtualisation.aggregation.dft.dft import Dft
import numpy as np

class DftControl():

    def __init__(self, buffer_size=50, window_length=5):
        self.buffer = RingBuffer(buffer_size)
        self.dftobj = Dft()
        self.window_length = window_length

    def control(self, data):
        self.buffer.add(float(data.value))
        if self.buffer.fillLevel() < self.window_length:
            return None
        result = self.dftobj.dft(self.convert(data), self.window_length)

        return result


    def convert(self, data):
        return np.asarray(data)