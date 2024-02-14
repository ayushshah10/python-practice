def prefixdecorator(prefix):
    def decorator_func(orig_func):
        def inner(*args,**kwargs):
            print(prefix,'Executed before',orig_func.__name__)
            res = orig_func(*args,**kwargs)
            print(prefix,'Executed after',orig_func.__name__)
        return inner
    return decorator_func

@prefixdecorator("PASS")
def orig_func(name,age):
    print('age:{} , name:{}'.format(age,name))

orig_func('Ayush Shah',21)
