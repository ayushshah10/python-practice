def fibo(n):
    x = 0
    y = 1
    while n>0:
        yield x
        x,y = y,x+y
        n-=1

ans = fibo(8)
print(next(ans))
print(next(ans))
print(next(ans))
print(next(ans))
print(next(ans))
print(next(ans))
print(next(ans))