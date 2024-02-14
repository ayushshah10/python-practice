def freq(l1):
    dict = {}
    for i in l1:
        if i in dict.keys():
            dict[i]+=1
        else:
            key = i
            value = 1
            dict[key] = value
    return dict

print(freq([1,2,23,4,2]))