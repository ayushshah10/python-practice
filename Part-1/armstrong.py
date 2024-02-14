def armstrong(num):
    li = [int(x) for x in str(num)]
    leng = len(li)
    res = 0
    for i in li:
        res += i**leng
    
    return res

print(armstrong(456))