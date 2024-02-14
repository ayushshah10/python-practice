def pairs(l1,target):
    numset = set(l1)
    res = []

    for i in numset:
        n2 = target - i
        if n2 in numset:
            res.append({n2,i})
    
    return res


l1 = [1,2,3,4,1,10]

print(pairs(l1,7))
