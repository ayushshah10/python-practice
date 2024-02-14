def fetch(l2,tr):
    res = [i[tr] for i in l2 if tr in i]
    return res


tr = 'Math'

l2 = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

res = fetch(l2,tr)
print(res)