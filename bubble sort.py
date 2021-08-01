# Bubble Sort in Python...
#time complexity of bubble sort is O(n^2)
#it is a simple comparision based algorithm ...
#in this compare two adjacent element of list ..if 1st elemnt is bigger than 2nd then swap them ...
#largest element of the list will be in last position .
#second largest element of the list will come in second last pos.
#this will untill,our list is sorted.
#in this we use two loops.
# if n=len(l)
#for i in range (n-1)
#for i in range (n-1)
def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
print(bubblesort([4,2,6,98,2]))



