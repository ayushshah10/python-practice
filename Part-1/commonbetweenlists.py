l1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [2, 4, 6, 8]

for i in l1:
    if i in l2:
        l1.remove(i)
print(l1)