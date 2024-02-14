set1 = {1,2,3,4}
set2 = {2,3,5,10}

set3 = set1 & set2
if len(set3)>0:
    print('there is common elements')
else:
    print('there is no common elements')
print(set3)