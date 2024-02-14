from collections import defaultdict

def merge(d1,d2):
    res = defaultdict(list)
    for d in d1,d2:
        for key in d:
            res[key].append(d[key])
    return dict(res)

l1 =  {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
l2 = {'x': 300, 'y': 'Red', 'z': 600}
res = merge(l1,l2)
print(res)

