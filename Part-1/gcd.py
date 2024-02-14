def gcd(x,y):
    i = 1
    while i<=x and i<=y:
        if x%i==0 and y%i==0:
            gc = i
        i+=1
    return gc
print(gcd(4,5))