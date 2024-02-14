from calendar import monthrange

def month(n):
    if n == 0:
        return []
    ll =[]  
    ll = month(n-1)
    
    if n%12>0:
         r1 = monthrange(2024,n%12)[1]
         temp = [i for i in range(1,r1+1)]
         ll.append(temp)
    else:
        r1 = monthrange(2024,12)[1]
        temp = [i for i in range(1,r1+1)]
        ll.append(temp)
    return ll

n = int(input()) 
ll = month(n)
print(ll)
# print(len(ll))