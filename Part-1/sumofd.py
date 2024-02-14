
l1 = list(input())
sums = sum(int(i) for n in l1 for i in str(n) if i.isdigit())
print(sums)
