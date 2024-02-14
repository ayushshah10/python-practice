# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# ans = list(filter(lambda x:(x%17==0 or x%13==0),nums))

# print(ans)


#to filter palindromes
# l2 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

# ans = list(filter(lambda x:(x[::-1] == x),l2))

# print(ans)
 
#sort list of lists based on sum

l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

ans = sorted(l1,key=lambda x : sum(x))

print(ans)