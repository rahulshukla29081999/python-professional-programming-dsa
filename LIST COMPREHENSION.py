number=[]   #normal method
for i in range(1,8):
    number.append(2**i)
print(number)


numbers=[2**i for i in range(1,8)] #list comprehension
print(numbers)

# if statement:- 


import math 
numbers=[49,64,72,100,121,]
squar_root=[math.sqrt for i in numbers if i%2==0]
print(numbers)    


# two-if statement
team1=["rahul","prakhar","pratham"]
team2=["anchal","pragya","vedika"]
team=[(i,j) for i in team1 for j in team2]
print(team)
