#roulette model

#18 red 18black 2 green

from random  import *
from statistics import *
from collections import *

#one way to model is type it out.. Too bad idea
print(choice(['red','red','black','black','green']))
# list can be repeated
print(choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2))
#we can make population variable
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
print(choice(population))

#if we  play six games
print([choice(population) for i in range(6)])

# or we can express by calling Choices which is same as above..
print(choices(population , k=6))

#we can use the counter property 
print(Counter(choices(population, k=6)))

#choices can build weight
print(Counter(choices(['red','black','green'], [18,18,2], k=6)))