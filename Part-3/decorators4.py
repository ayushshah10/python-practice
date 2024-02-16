def decorator(func):
    def inner(n):
        if n<0:
            raise ValueError('Negative Value')
        return func(n)
    return inner

@decorator
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(10))
