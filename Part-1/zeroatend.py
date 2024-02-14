li =  [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
l1 = []
l2 = []

for i in li:
    if i ==0:
        l2.append(i)
    else:
        l1.append(i)

l1.extend(l2)

print(l1)