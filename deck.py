
from random  import *
from statistics import *
from collections import *

deck = Counter(tens=16,lows=36)

deck = list(deck.elements())

deal = sample(deck,k=20)
print(Counter(deal))

deal = sample(deck,k=52)
print(Counter(deal))

remainder = deal[20:]
print(Counter(remainder))

