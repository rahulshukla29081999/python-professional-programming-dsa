#separate even or odd in list

def getEveOdd(l):
    even=[]
    odd=[]
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
        return even,odd
l=[10,20,30,41,55]

even,odd=getEveOdd(l)
print(even)
print(odd)

