def fibo(n):
    x = 0
    y = 1
    yield x
    while n>0:
        x,y = y,x+y
        n-=1
        yield x



for i in fibo(7):
    print(i)