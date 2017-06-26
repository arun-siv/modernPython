from heapq import merge
from itertools import islice

l1 = [10,9,8]
l2 = [8,4,2]

m = merge(l1,l2, reverse=True)
print(list(islice(m, 2)))