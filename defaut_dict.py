from collections import defaultdict

d = {'raymond' : 'red'}

e = defaultdict(lambda : 'black')

e['raymond'] = 'red'
print(e)

print(e['Rachel'])

d = defaultdict(set)
d['t'].add('Tom')
d['m'].add('Mary')
d['t'].add('Tom')
d['t'].add('Tim')

print(d)

#default dict creates a new container to store elements with a common failure

print(d['q'])


l = defaultdict(list)
l['t'].append('Tom')
l['t'].append('Tom')
print(l)

def con_lower(name):
    return name.lower()


from pprint import pprint
names = ['Jane', 'David', 'Darlene', 'Beatrice', 'Wallace', 'Tom', 'Suzane', 'Davin', 'Betty', 'Mary', 'Sandy' , 'Becky', 'Shelly', 'Micheal', 'Tom', 'Susan']
new_names = sorted([name.lower() for name in names ])
pprint(new_names, width=80)

d = defaultdict(list)
for name in new_names:
    feature = name[0]
    d[feature].append(name)

pprint(d)

pprint(sorted(new_names, key=len))