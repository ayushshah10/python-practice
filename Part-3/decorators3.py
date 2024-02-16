def decorator(function):
    def inner():
        func = function()
        ans = func.upper()
        return ans
    return inner

@decorator
def orig():
    return 'red'

print(orig())