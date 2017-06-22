from pprint import pprint
from itertools import zip_longest
from statistics import mean
print(list(zip_longest('abcdef', 'ghijklm')))

m =[
    [10,20],
    [30,40],
    [50,60]
]

# 3 row 2 coln

pprint(list(zip(*m)), width=20) # transposes

for row in  m:
    for col in row:
        pprint(col, width=10)


pprint([x for row in m for x in row])


group = [(10,41,23),(11,42,5),(20,32,4),(12,40,12),(22,30,9),(21,36,3)]
pprint(tuple(map(mean, list(zip(*group)))))