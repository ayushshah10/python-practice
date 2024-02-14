def longestprefix(l1):
    if not l1:
        return ""
    
    minl = min([len(st) for st in l1])
    
    for i in range(minl):
        chars = set([word[i] for word in l1])

        if len(chars)>1:
            return l1[0][:i]
    return l1[0][:minl]

print(longestprefix(['apshah','payush']))