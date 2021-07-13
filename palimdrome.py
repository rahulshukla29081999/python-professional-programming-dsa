def isPalimdrome(s):#function which returns  the reverse of the string ...
   return s[::-1]

#driver code

s="rahul"
ans= isPalimdrome(s)
if ans:
    print("yes")
else:
    print("false")
