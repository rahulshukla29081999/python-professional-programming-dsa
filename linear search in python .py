#Linear Search In Python...
def linear_search(l,n,len):
    for i in l:
        if n==i:
            return i
        else:
            return-1


l=[2,0,6,1,5,9]
n=15
len=len(l)
a=linear_search(l,n,len)
if a ==-1:
    print("the element is not found")
else:
    print("the index element",a)