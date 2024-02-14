def strobo(n):
    if n==0:
        return ['']
    elif n==1:
        return['1','0','8']
    else:
        res = list()
        rem = list(strobo(n-2))
        for i in rem:
            res.append("1" + i + "1")
            res.append("6" + i + "9")
            res.append("8" + i + "8")
            res.append("9" + i + "6")
    return res
print(strobo(6))