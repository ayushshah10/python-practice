def insertat(x,l1,pos):
    return l1[:pos-1] + [x] + l1[pos-1:] 

l1 = [2,3,4,1,4,6]
print(insertat(10,l1,3))