n=int(input())
for i in range(0,n):
    a=str(input())
    l=len(a)
    
    if(l>10):
        print(a[0],end="")
        print(l-2,end="")
        print(a[-1])
    else:
        print(a)