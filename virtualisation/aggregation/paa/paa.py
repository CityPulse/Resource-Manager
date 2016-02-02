__author__ = 'Daniel Puschmann'

import numpy as np
import math
import bottleneck as bn

class Paa():

    def __init__(self):
        pass

    def process(self, window, output_length):
        data = np.array_split(window, output_length)
        result = []
        for segment in data:
            mean = bn.nanmean(segment)
            if math.isnan(mean):
                result.append(0)
            else:
                result.append(mean)
        result = np.array(result)
        return result
