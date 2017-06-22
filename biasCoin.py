from random  import *
from statistics import *
from collections import *

pop =['heads', 'tails']

cwgt = [0.6,1.0] # cumulative weight of a biased coin

oneSpin = choices(pop, cwgt)
print(oneSpin)

n = 10000
trial = lambda: choices(pop, cwgt ,k=7).count('heads') >= 5
av = sum(trial() for i in range(n))/n
print(av)