#Create a list (new_list) of overlapping values

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []

 #check mutually exclusive values
for i in a:
    for j in b:
        if i == j:
            if i not in new_list:
                new_list.append(i)
print(new_list)
