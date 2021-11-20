import math

class Math(object):
    def __init__(self, data):
        self.mean = self.mean(data)
        self.std = self.std(data, self.mean)
    
    def mean(self, data):
        res = 0
        for e in data:
            res = res + e
        return res / len(data)

    def std(self, data, mean):
        ret = 0
        for d in data:
            if math.isnan(d) is False:
                ret = ret + (d - mean)**2
        ret = math.sqrt((ret / (len(data) - 1)))
        return ret
