#get smaller elements in lists....

def smallElement(l,x):
    res=[]
    for i in l:
        if i<x:
            res.append(i)
        return i
  
    l=[10,20,8,9,6,5,101]
    x=10
    print(smallElement(l,x))
