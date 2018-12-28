#Remove duplicates using sets()
import random

a = ''
b = ''
chars = 'abcdefghijklmnopqrstuvqxyz1234567890'

for i in range(0, random.randint(8, 32)):
    a += chars[random.randint(0, len(chars)-1)]

for i in range(0, random.randint(8, 32)):
    b += chars[random.randint(0, len(chars)-1)]

print('a is equal to:   ', a)
a = set(a)
print('a without duplicates:    ', a)
print('b is equal to:   ',b)
b = set(b)
print('b without duplicates:    ', b)




print('Intersection is:    ', a.intersection(b))
