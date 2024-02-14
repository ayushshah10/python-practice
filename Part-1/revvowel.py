def rev(strr):
    res = ""
    vow = ""
    for i in strr:
        if i in 'aeiouAEIOU':
           vow+=i

    for i in strr:
        if i in 'aeiouAEIOU':
            res+=vow[-1]
            vow = vow[:-1]
        else:
            res+=i 

    return res
print(rev('ayushshah'))