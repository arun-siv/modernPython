from typing import *
from collections import OrderedDict, namedtuple
x: int = 10

#this function exibits ducktyping

def f(x: int,y: int) -> int:
    return x+y

print(f(10,20))
print(f(10,3))

y: OrderedDict = OrderedDict()


def g(x: List[int] ,y: Optional[int]=None) -> None:
    if y is None:
        y = 20
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

print(g([1,2,3]))
print(g('abcde'))
print(g((33,4,5,3)))


ht = [8,29,39.0] # type: List[float]
t  = ('Raymond', 83*12+1) # type: Tuple[str,int]

print(f'the value of x is {x} today')
