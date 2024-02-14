res = ""
for i in range(0,7):
    for j in range(0,7):
        if(j==1 or j==5 or (i==2 and (j==2 or j==4)) or (i==3 and j==3)):
            res = res + '* '
        else:
            res = res + "  "
    res = res + '\n'

print(res)

