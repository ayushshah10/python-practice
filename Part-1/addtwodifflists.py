def addtwo(l1,l2):
    dlen = len(l1) - (len(l2)-1)
    for i in range(len(l1),0,-1):
        if i-dlen<0:
            break
        else:
            l1[i-1] = l1[i-1] + l2[i-dlen]
    return l1

l1 = [2,3,4,1,6]
l2 = [2,3,1,4]
print(addtwo(l1,l2))