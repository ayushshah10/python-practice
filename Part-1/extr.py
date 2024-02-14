from calendar import monthrange

year = 2024

def month(year,n,ll):
    if n == 0:
        return []    
    n1 = n
    while n1>12:
        year = year+1
        n1 -= 12

    print(year)    
    if n%12>0:
         r1 = monthrange(year,n%12)[1]
         temp = [i for i in range(1,r1+1)]
         ll.append(temp)
    else:
        r1 = monthrange(year,12)[1]
        temp = [i for i in range(1,r1+1)]
        ll.append(temp)
    return month(year,n-1,ll)

n = int(input()) 
ll =[]  
month(year,n,ll)
print(ll[::-1])
# print(len(ll))