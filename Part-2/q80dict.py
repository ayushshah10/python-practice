
dict2 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
l1 = dict2.values()
max = 0

for i in l1:
    if i > max:
        max = i
    
ans = [key for key in dict2 if dict2[key]==max]

print(ans)