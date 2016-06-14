from buffer import RingBuffer


class RewardAndPunishment():
    """Reward and Punishment mechanism inspired by "Modeling and Assessing Quality of Information in Multisensor Multimedia Monitoring Systems" by Hoassain et al. """

    def __init__(self, window):
        self.window = window
        self.buffer = RingBuffer(window)
        self.reward = 1.0
        self.lowest = self.reward
        for i in xrange(0, window):
            self.update(True)

    def update(self, truthHold):
        alpha_w_minus_1 = float(len(filter(lambda x: x == 1, self.buffer.items[1:])))
        w_minus_1 = self.buffer.fillLevel() - 1
        alpha = 0.0
        if truthHold != 0:
            alpha = 1.0
        self.buffer.add(alpha)

        if w_minus_1 > 0:
            r_p = (alpha_w_minus_1 / w_minus_1) - ((alpha_w_minus_1 + alpha) / (w_minus_1 + 1))
            # r_p = (alpha_w_minus_1 / w_minus_1) - ((alpha_w_minus_1 + alpha) / (self.window))
            self.reward -= 2 * r_p
            self.lowest = min(self.lowest, self.reward)
        # r_p = (alpha_w_minus_1 + alpha) / (w_minus_1)
        # self.reward = r_p

        # print alpha_w_minus_1, w_minus_1, ":", truthHold, self.reward, r_p, "--> %f" % self.value(), "lowest %f" % self.lowest
        # print "%s %d/%d: %.3f --> %.3f (lowest %.3f)" % (truthHold, alpha_w_minus_1, w_minus_1, r_p, self.reward, self.lowest)
        else:
            if truthHold:
                self.reward = 1.0
            else:
                self.reward = 0.0

    def value(self):
        if abs(self.reward) < 0:
            return 0
        elif abs(self.reward) > 1:
            return 1
        return abs(self.reward)  # * 2 - 1


def memory_usage_psutil():
    import psutil, os
    process = psutil.Process(os.getpid())
    mem = float(process.memory_info()[0]) #/ float(2 ** 20)
    return mem

def memory_usage_resource():
    import resource, sys
#    rusage_denom = 1024.
    rusage_denom = 1.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom


"""
if __name__ == "__main__":
    import sys
    mems = []
    rps = []
    # mems.append((0, memory_usage_resource()))
    mem_method = memory_usage_psutil
    first = mem_method()
    last = 0
    new = 0
    for x in xrange(1, 2**20):
        #rp = RewardAndPunishment(10)
        rps.append(RewardAndPunishment(10))
        new = mem_method()
        if last != new:
            last = new
            # print x, new
            mems.append((x, new))
    #print first, mems
    mems_size = sys.getsizeof(mems)

    # export
    # f = open("mem_r_and_b.csv", "w")
    # for x, y in mems:
    #     # print x, y, (y - mems_size - first) / x
    #     f.write("%d;%f;%f\n" % (x, y, (y - mems_size - first) / x))
    #
    # # print mems_size
    # f.close()
    # print "done"

    # plot
    import matplotlib.pyplot as plt
    number = []
    value = []
    for x, y in mems:
        number.append(x)
        # value.append((y - mems_size - first) / x)
        value.append(y)
    value = map(lambda _x: _x - first, value)
    # print number[0:30], value[0:30]
    y_labels = []
    y_ticks = []
    for i in xrange(0, 1000, 100):
        y_ticks.append(i * 2**20)
        y_labels.append(str(i) + " MB")
    y_ticks.append(2**30)
    y_labels.append("1 GB")
    plt.plot(number, value)
    plt.yticks(y_ticks, y_labels)
    plt.ylabel("memory usage")
    plt.xlabel("number of instances")
    plt.savefig("rp_mem_consumption.pdf", format='pdf')
    #plt.show()
"""


if __name__ == "__main__":
    import random
    import datetime
    import matplotlib.pyplot as plt
    import numpy as np

    window_size = 10
    runs = 2**20
    inputs = []
    repeations = 1000

    for i in xrange(0, 10):
        inputs.append(random.random() > 0.5)

    totals = []
    speed = []
    for _ in xrange(0, repeations):
        rp = RewardAndPunishment(window_size)
        start_time = datetime.datetime.now()
        for x in xrange(0, runs):
            rp.update(x % window_size)
        end_time = datetime.datetime.now()
        t = end_time - start_time
        s = t.seconds
        ms = t.microseconds
        total = (ms + (s * 1000000.)) / 1000.
        totals.append(total)
        print runs, "in", total, "ms."
        #print t
        print t.seconds, t.microseconds
        print runs / total, "per ms."
        speed.append(runs/total)
        print

    s = sum(totals)
    print runs * repeations / s, "on average"
    _X = speed
    _X.sort()
    # _min = int(min(_X))
    # _max = int(max(_X))
    # step = (_max - _min) / (len(_X)-1)
    # xvalues = range(int(min(_X)), int(max(_X)), step)
    # print xvalues, _X
    # totals = map(lambda x: x/s, totals)
    print "norm", totals, "sum", sum(totals)
    # cdf = np.cumsum(totals)
    # counts, bin_edges = np.histogram(totals, 20, normed=False)
    # cdf = np.cumsum(counts)
    # print "cdf", cdf
    #plt.plot(totals)
    # plt.plot(np.array(xvalues), np.array(cdf))
    # plt.plot(bin_edges[1:], np.array(cdf))
    yvals = np.arange(len(_X))/float(len(_X))
    plt.plot(_X, yvals)
    plt.ylabel("cumulative probability")
    plt.xlabel("number of runs per microsecond")
    plt.savefig("rp_time_consumption.pdf", format='pdf')
    #plt.show()

