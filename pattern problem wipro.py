# for i in range(4):#****
#     print('*'*4)  #****
                    #****
                    #****


#    ****
#    *  *
#    *  *
# #    ****
# def pattern(n):
   
#     for i in range(1,n+1):
#         if i==1 or i==4:
#             print(4*'*')
#         else:
#             print("*"+(n-2)*''+'*')
# print(pattern(4))


# *
# **
# ***
# # ****
# def pattern(n):
#     for i in range(1,n+1):
#         if i==1:
#             print('*'*(n-3))
#         elif i==2:
#             print('*'*(n-2))
#         elif i==3:
#             print('*'*(n-1))
#         else:
#             print('*'*n)
# print(pattern(4))


#     *  
#    ***
#   *****
#  *******
def pattern(n):
    for i in range(1,n+1):
        if i==1:
            print(''+''+''+'*'+''*3)
        elif i==2:
            print(''*2+'***'+''*2)
        elif i==3:
            print(""+'*'*5+'')
        else:
            print('*'*n)
print(pattern(4))