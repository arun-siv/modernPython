from random import *
a = seed(8373438)

print(random())
print(random())

a = seed(8373438)
print(random())
print(random())

print(uniform(1000,1100))
#expovariate
#gauss
#triangular

from statistics import mean, stdev
data = [triangular(1000,1100) for i in range(1000)]
print(mean(data))
print(stdev(data))