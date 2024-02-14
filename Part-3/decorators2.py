import time

def checkexpiration(expirytime):
    print('in checkexpiration')
    def decorator(func):
        print('in decorator')
        cache = {}
        def inner(*args,**kwargs):
            print('in inner')

            key = (*args,*kwargs.items())
            # print(key)

            if key in cache:
                value,timestamp = cache[key]
                print(value)
                if time.time()-timestamp<expirytime:
                    return value
            result = func(*args,**kwargs)
            cache[key] = (result,time.time())
            return result
        return inner
    return decorator


@checkexpiration(expirytime=5)
def original(n1,n2):
    return n1*n2

print(original(24,33)) 
            
print(original(24,33)) 

