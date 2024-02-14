dict1 = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

l1  = dict1.values()
dict2 = {}

for i in l1:
    if i in dict2:
        dict2[i]+=1
    else:
        value = 1
        key = i
        dict2[key]=  value

print(dict2)