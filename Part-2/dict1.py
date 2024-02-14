dict1 = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}


dict1['Math'] = [i+1 for i in dict1['Math']]

dict1['Chemistry'] = [i-2 for i in dict1['Chemistry']]

print(dict1)