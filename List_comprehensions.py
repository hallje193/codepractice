#List Comprehensions

#Given the following list, create new list with only even elements.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#List even elements
#even = []
#for i in a:
#    if i % 2 == 0:
#        even.append(i)


#Single-line solution for listing even elements
even = [i for i in a if i% 2 == 0]

print(even)
