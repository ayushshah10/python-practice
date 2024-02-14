def makebold(func):
    def inner():
        print("inside makebold inner")
        func()
    return inner

def makeitalic(func):
    def inner():
        print("inside makeitalic inner")
        func()
    return inner

def makeunder(func):
    def inner():
        print("inside makeunder inner")
        func()
    return inner


@makebold
@makeitalic
@makeunder
def orig_func():
    print("original function")

orig_func()