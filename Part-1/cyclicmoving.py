def cyclic(l1,n):
    t1 = l1[:n]
    t2 = l1[n:]

    t2.extend(t1)
    return t2
n = int(input())
l1 = [2,3,4,5,6,1]
print(cyclic(l1,n))