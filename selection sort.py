def selection_sort(l):          # selectio sort 
    n=len(l)                    # worst case is O(n^2)
    
    for i in range(n-1):
        min_index=i

        for j in range(i+1,n):
            if l[j] < l[min_ind]:
                min_ind=j
        l[min_index],l[i]=l[i],l[min_ind]


  
