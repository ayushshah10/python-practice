def decorator_func(original):
    print("in decorator_func")

    def inner():
        print("in inner func")
        return original()

    return inner

@decorator_func
def orig_func():
    print('original function')


#abc = decorator_func(orig_func)
#abc()
orig_func()