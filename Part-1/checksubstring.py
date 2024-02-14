def check(l1,substr):
    if any(substr in i for i in l1):
        return True
    else:
        return False


l1 = ['red', 'black', 'white', 'green', 'orange']
substr = 'ite'
print(check(l1,substr))