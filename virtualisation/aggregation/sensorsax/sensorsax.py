from __future__ import division
from virtualisation.misc.log import Log

__author__ = 'Daniel Puschmann'
import numpy as np
from scipy.stats import norm
import string

# paa tranformation, window = incoming data, string_length = length of outcoming data

class Sax(object):

    def __init__(self, alphabet_size):
        self.alphabet_size = alphabet_size
        self.breakpoints = self.gen_breakpoints(alphabet_size)
        self.epsilon = 0.0001


    def sax(self, window, output_length):

        # if self.all_identical(window):
        #     return None
        if np.array(window).std() < self.epsilon:
            middle_letter = int(self.alphabet_size/2)
            return [''.join([string.ascii_letters[middle_letter] for _ in range(len(window))])]
        sax = self.to_sax(self.to_paa(self.normalize(window), output_length))
        # return vocabToCoordinates(len(window),output_length,sax[0],4)
        #        return vocabToCoordinates(output_length,output_length,sax[0],4)
        return sax

    def normalize(self, data):
        data2 = np.array(data)
        data2 -= (np.mean(data))
        data2 *= (1.0 / data2.std())
        return data2


    def to_paa(self, data, string_length):
        data = np.array_split(data, string_length)
        return [np.mean(section) for section in data]


    def gen_breakpoints(self, symbol_count):
        breakpoints = norm.ppf(np.linspace(1. / symbol_count, 1 - 1. / symbol_count, symbol_count - 1))
        breakpoints = np.concatenate((breakpoints, np.array([np.Inf])))
        return breakpoints


    def to_sax(self, data):
        locations = [np.where(self.breakpoints > section_mean)[0][0] for section_mean in data]
        return [''.join([string.ascii_letters[ind] for ind in locations])]


    def createLookup(self,symbol_count, breakpoints):
        return self.make_matrix(symbol_count, symbol_count, breakpoints)


    def make_list(self, row, size, breakpoints):
        mylist = []
        for i in range(size):
            i = i + 1
            if abs(row - i) <= 1:
                mylist.append(0)
            else:
                v = breakpoints[(max(row, i) - 2)] - breakpoints[min(row, i) - 1]
                mylist.append(v)
        return mylist


    def make_matrix(self, rows, cols, breakpoints):
        matrix = []
        for i in range(rows):
            i = i + 1
            matrix.append(self.make_list(i, cols, breakpoints))
        return matrix
