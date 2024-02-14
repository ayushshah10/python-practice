tu1 = (1, 2, 3, 4)
tu2 = (3, 5, 2, 1)
tu3 = (2, 2, 3, 1)
tu4 = ()

for i in range(len(tu1)):
    tu4  = tu4+(int(tu1[i]+tu2[i]+tu3[i]),)

print(tu4)
