#last occurence of an element using binary search in python...
def binary_last_occ(l,x):
    low= 0
    high= len(l)-1
    while low <=high:
        mid=(low+high)//2               #time complexity is O(N)...
        if l[mid]<x:                    # SPACE COMPLEXITY IS O(1)...
            low=mid+1
        elif l[mid]>x:
            high =mid-1
        else:
            if l[mid]==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low =mid+1
    return -1
l=[10,10,20,20,20,30,30]
x=20
a=binary_last_occ(l,x)
print(a)

