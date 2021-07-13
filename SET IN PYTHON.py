#SET IN PYTHON...
#DISTINCT...UNOREDER...NO INDEXING...
#UNINION ...INTERSSECTON...DEFFERENCES  ARE VERY FAST IN SET...
#USES HASHING INTERNALLY ...

# s1={1,2,3,4,5,6,7}
# print(s1)

# s1={10,20,30}
# print(s1)
# s2={20,30,40}
# print(s2)
# s3={}
# print(type(s3))
# s4=set()
# print(s4)
# print(type(s4))

# python program to  set insert 
s={10,20}
s.add(30)
print(s)
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update({60,70},[80,90])
print(s)