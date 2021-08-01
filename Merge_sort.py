

def merge_sort(l):
    if len(l)>1:
        mid=len(l)//2
        L=l[:mid]
        R=l[mid:]
        merge_sort(L)
        merge_sort(R) 
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                l[k]=L[i]
                i=i+1
                k=k+1
                
            else:
                l[k]=R[j]
                j=j+1
                k=k+1
        while i<len(L):
            l[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            l[k]=R[j]
            j=j+1
            k=k+1

a=[5,4,9,2,74,2,1,55,6,2]
merge_sort(a)
print(a)



