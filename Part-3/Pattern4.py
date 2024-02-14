res = ""
print("enter a number according to below chart to print respective pattern\n")
print('Enter 1 to print A pattern\n')
print('Enter 2 to print D pattern\n')
print('Enter 3 to print P pattern\n')
print('Enter 4 to print N pattern\n')

inp = int(input())

if inp ==1:
    for i in range(0,7):
        for j in range(0,7):
            if((j==1 or j==5 )and i>0) or (i==0 and j>1 and j<5) or (i==3 and j>1 and j<5):
                res = res + "* "
            else:
                res = res + "  "
        res = res + '\n'
    print(res)

res = ""

if inp == 2:
    for i in range(0,7):
        for j in range(0,7):
            if j==1 or (j==5 and i!=0 and i!=6) or (i==0 and j>=0 and j<5) or (i==6 and j>=0 and j<5):
                res = res + "* "
            else:
                res = res + "  "
        res = res + '\n'
    print(res)

res = ""

if inp == 3:
    for i in range(0,7):
        for j in range(0,7):
            if j==0 or (i==3 and j<4) or (i==0 and j<4) or ((j==6 and i!=3)and (i>0 and i<4)):
                res = res + "* "
            else:
                res = res + " "
        res = res + '\n'
    print(res)

res = ""
    
if inp == 4:
    for i in range(0,7):
        for j in range(0,7):
            if j==0 or j==i or j==6:
                res = res + "* "
            else:
                res = res + "  "
        res = res + '\n'
    print(res)

# (j==6) and (i>0 and i<4)