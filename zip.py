from pprint import pprint
from itertools import zip_longest
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