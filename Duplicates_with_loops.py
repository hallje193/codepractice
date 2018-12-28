#Remove duplicates using loops
import random

a = ''
b = ''
chars = 'abcdefghijklmnopqrstuvqxyz1234567890'

for i in range(0, random.randint(8, 32)):
    a += chars[random.randint(0, len(chars)-1)]

for i in range(0, random.randint(8, 32)):
    b += chars[random.randint(0, len(chars)-1)]

a_clean = ''
for i in range(0, len(a)-1): #Last value in range is not inclusive.
    if a[i] not in a_clean:
        a_clean += a[i]

print(a)
print(a_clean)

b_clean = ''
for i in range(0, len(b)-1): #Last value in range is not inclusive.
    if b[i] not in b_clean:
        b_clean += b[i]
        print(b_clean)
print(b)
print(b_clean)
