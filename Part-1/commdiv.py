def commondiv(x,y):
    count = 0
    for i in range(1,min(x,y)+1):
        if x%i==y%i==0:
            count+=1
    return count
print(commondiv(12,24))