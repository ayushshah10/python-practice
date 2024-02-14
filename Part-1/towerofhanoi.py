def towerofhanoi(n,source,dest,mediate):
    if n == 1:
        print("Move disk 1 from source",source,"to destination",dest)
        return
    
    towerofhanoi(n-1,source,mediate,dest)
    print ("Move disk",n,"from source",source,"to destination",dest)    
    towerofhanoi(n-1,mediate,dest,source)


n = 4
towerofhanoi(n,'A','B','C')