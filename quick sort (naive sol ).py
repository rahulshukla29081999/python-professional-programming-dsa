def partition(l,p): # naive solution for quick sort ...
    n=len(l)        
    l[p],l[n-1]=l[n-1],l[p]
    temp=[]
    for i in l:
        if i<=l[n-1]:
            temp.append(i)
    for i in l:
        if i>l[n-1]:
            temp.append(i)


    for i in range(len(l)):
        l[i]=temp[i]
    return temp
l=[5,2,3,45,9]
p=0
k=partition(l,p)
print("sorted  array is",k)
