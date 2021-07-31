def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l = [2,10,8,7]
  
bubblesort(l)
  
print ("Sorted array is:")
for i in range(len(l)):
    print ("% d" % l[i],end="")

