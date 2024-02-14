# nums = [1,2,3,4,5]

# res = list(map(lambda x : x**3,nums))

# print(res)

# l1 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

# res = list(filter(lambda x:x if x==x[::-1] else None,l1))

# print(res)

l1 =  [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

ans = dict(map(lambda x : (x,list(l1).count(x)),l1))

print(ans)