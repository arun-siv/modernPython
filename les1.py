x = 10

print(f'the value of x is {x}')

from collections import Counter

d = Counter()
print(d['dragon'])

d['dragon'] += 1
print(d)

e = Counter('red blue red red green blue red blue green yellow orange'.split())
print(e.most_common(1))
print(e.most_common(2))
print(e.most_common())

print(list(e.elements())) # we get back all our colors