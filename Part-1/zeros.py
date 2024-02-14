def facto(n):
    x = int(n//5)
    y = x

    while x>0:
        x /=5
        y += int(x)
    return y
print(facto(19))