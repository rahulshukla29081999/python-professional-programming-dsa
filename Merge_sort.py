# def mergeSort(myList):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]

#         # Recursive call on each half
#         mergeSort(left)
#         mergeSort(right)

#         # Two iterators for traversing the two halves
#         i = 0
#         j = 0
        
#         # Iterator for the main list
#         k = 0
        
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#               # The value from the left half has been used
#               myList[k] = left[i]
#               # Move the iterator forward
#               i += 1
#             else:
#                 myList[k] = right[j]
#                 j += 1
#             # Move to the next slot
#             k += 1

#         # For all the remaining values
#         while i < len(left):
#             myList[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             myList[k]=right[j]
#             j += 1
#             k += 1

# myList = [54,26,93,17,77,31,44,55,20]
# mergeSort(myList)
# print(myList)


def merge_sort(l):
    if len(l)>1:
        mid=len(l)//2
        L=l[:mid]
        R=l[mid:]
        merge_sort(L)
        merge_sort(R) 
        i=j=k=0
        while i<len(L) and i<len(R):
            if L[i]<=R[i]:
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



