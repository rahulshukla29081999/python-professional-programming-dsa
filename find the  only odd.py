# find the only odd ...
def findOdd(l):
    res=None
    for x in l:
        count=l.count(x)
        if x%2!=0:
            res=x
            break
    return res
l=[10,20,30,10,20]
print(findOdd(l))
