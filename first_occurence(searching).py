#first occurence of index ...
def first_occurence(l,x):
    for i in range(len(l)):
       if  l[i]==x:
        return i
    return -1
l=[10,10,20,20,20]
x=50
a=first_occurence(l,x)
print(a)