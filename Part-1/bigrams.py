sl = ['Sum all the items in a list', 'Find the second smallest number in a list']

# l2 = [tuple(i,i+1) for i in sl]
for i in range(len(sl)):
    l1 = sl[i].split()
    tl = [tuple(l1[i],l1[i+1]) for i in l1]


print(tl)