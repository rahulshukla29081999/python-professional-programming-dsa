#pattern searching in python ...

txt="geeksforgeeks"
pat="geeks"
pos=txt.find(pat)
while pos>=0:
    print(pat)
    pos=txt.find(pat,pos+1)
