from random import choice, choices, shuffle , sample

outcomes = ['win', 'lose', 'play again', 'draw', 'double win']

print(choice(outcomes))

print(choices(outcomes , k=10))

from collections import Counter
print(Counter(choices(outcomes, k=20)))

print(Counter(choices(outcomes, [5,4,3,2,1], k=1000)))

shuffle(outcomes)
print(outcomes)

print(sample(outcomes, k = 5))


print(sorted(sample(range(1,56), k=6))) # sample no repeating

#choice and sample 
print(sample(outcomes,k=1)[0]) # same as choice ... 

#sample and shuffle
print(sample(outcomes, k=len(outcomes))) # shuffle(outcomes) special case of sample k=len(outcomes)