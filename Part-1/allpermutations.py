def permute(l1):
    res = []
    
    if len(l1) == 0:
        return []
    if len(l1) == 1:
        return [l1]
    
    for i in range(len(l1)):
        x = l1[i]
        newl = l1[:i] + l1[i+1:]

        for p in permute(newl):
            res.append([x]+p)
    return res

l1 = [2,3,4,1,5]
print(permute(l1))
