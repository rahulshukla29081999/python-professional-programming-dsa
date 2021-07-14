#first occurence of element using binary search...
def binary_first_occurence(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low=mid+1
        elif l[mid]>x:
            high=mid-1
        else:
            if l[mid]==0 or l[mid-1]!=l[mid]:
                return mid 
            else:
                high =mid-1
    return -1
l=[10,20,20,30,30]
x=50
a=binary_first_occurence(l,x)
print(a)
