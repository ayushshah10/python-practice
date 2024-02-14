tu = (2,3,4,1,5)
tu = tu + (10,)
# print(tu)

l1 = list(tu)
l1.remove(5)

tu1 = tuple(l1)
tu2 = ()
for i in range(len(tu1)-1,0,-1):
    tu2 = tu2 + (tu1[i],) 

tu2 = tu2 + (tu1[0],)

print(tu2)

mul = 1
for i in tu1:
    mul = mul *  i
print(mul)