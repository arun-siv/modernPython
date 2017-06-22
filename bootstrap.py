
timings = [7.18, 8.59, 12.24, 7.39, 8.16,8.68,6.98,8.31,9.06,7.06,7.67,10.02,6.87,9.07]
from random  import *
from statistics import *
from collections import *

from statistics import mean, stdev

def bootstrap(data):
    return choices(data, k=len(data))
n = 10000
means = sorted(mean(bootstrap(timings)) for i in range(n))

print(means[500])
print(means[-500])