def binary(arr,low,high,target):
    while high>low:
        mid = high+low//2

        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            return binary(arr,0,mid-1,target)
        elif arr[mid]<target:
            return binary(arr,mid,high,target)
        else:
            return -1

arr = [1,2,3,4,5,6,10]
n = binary(arr,0,len(arr)-1,6)

if n!=-1:
    print("target element is in ",n,"position")
else:
    print("element not found")