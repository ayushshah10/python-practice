from collections import defaultdict

def merge(*dicts):
    res = defaultdict(list)

    for d in dicts:
        for key in d:
            res[key].append(d[key])
    return res

dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}

ans = merge(dict1,dict2)

print(ans)