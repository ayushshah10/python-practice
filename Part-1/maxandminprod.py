def findmax(l1):
    max = 0
    for i in l1:
        prod = i[0]*i[1]
        if max < prod:
            max = prod

    return max


def findmin(l1):
    min = 99999
    for i in l1:
        prod = i[0]*i[1]
        if min>prod:
            min = prod
    return min
l1 = [(2, 7), (2, 6), (1, 8), (4, 9)]
print(findmax(l1))
print(findmin(l1))