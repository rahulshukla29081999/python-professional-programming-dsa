# def fun(n):      #3
#     if n==0:     #2
#         return   #1
#     print(n)     #1
#     fun(n-1)     #2
#     print(n)     #3        #output...
# #          
# # fun(3) 
# #problem 2..
# def fun(n):    #1
#     if n==0:   #2
#         return #1
#     fun(n-1)   #3
#     print(n)   #1
#     fun(n-1)   #2
# fun(3)         #1            #output..

# n to 1 using recursion...
# def fun(n):
#     if n==0:
#         return
#     print(fun(n-1))
#     print(n)
# fun(5)

#sum of n digits...
def dSum(n):
    if n<10:
        return n
    return dSum(n//10)+n%10
print(dSum(5555))       # 18 is the output..