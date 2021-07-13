# #set in python...
# s1={1,2,3,4}
# print(s1)
# s2=set([20,30,40])
# print(s2)
# s3={}
# print(type(s3))
# set=set()
# print(set)
# print(type(set))

# #{}is used for both dictionary and set...
# s={10,20}
# s.add(30)
# print(s)
# s.add(40)
# print(s)
# s.add(50)
# print(s)
# s.update([60,70])
# print(s)
# s.update({80,90},[100,110])
# print(s)
# s.update({120,130})
# print(s)

# #removal operation on set 
# s={10,20,30,40}
# s.discard(30)
# print(s)
# s.discard(50)
# print(s)
# s.remove(40)
# print(s)
# s.clear()
# print(s)
# s.add(50)
# print(s)


# #some other operation
# s={10,20,30,40}
# print(len(s))
# print(30 in s)
# print(50 in s)



#operation on two  set 

# s1={2,4,6,8}
# s2={3,6,9,}
# print(s1|s2)
# print(s1 & s2)
# print(s1-s2)
# print(s1^s2)
# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

#operation on two set (part 2)

# s1={2,4,6,8}
# s2={4,8}
# print(s1.isdisjoint(s2))
# print(s1>s2)
# print(s1>=s2)
# print(s1>s2)