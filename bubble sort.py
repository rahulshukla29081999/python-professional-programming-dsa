def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
print(bubblesort([4,2,6,98,2]))



