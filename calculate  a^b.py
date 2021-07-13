#in recursion a^n=a^n* a^n-1
#in iteration a^n=a*a*a*a*a*a*a......n times 
# now we are calculating the a^b by only recursion...
p=3
q=5
def power(a,b):
    if (b==0):
        return 1
    else:
       return a*power(a,b-1)