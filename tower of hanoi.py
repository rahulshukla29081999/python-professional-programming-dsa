#tower of hanoi in python...
# def TOH(n,A,B,C):
#     if n==1:
#         print("move 1 from",A, "to",C)
#     else:
#         TOH(n-1,A,C,B)
#         print("move 2 from",A ,"to", C)
#         TOH(n-1,B,A,C)
# TOH(3,'A','B','C')



# def Toh(n,a,b,c):
#     if n==1:
#         print("move 1 from",a,'to',c)
#     else:
#         Toh(n-1,a,c,b)
#         print("move 2 form",a, 'to', c)
#         Toh(n-1,b,a,c)
# Toh(2,'a','b','c')



def toh(n,a,b,c):
    if n==1:
        print("move 1 from", a, 'to', c)
    else:
        toh(n-1,a,c,b)
       
        print('move 2 from',a ,'to', c)
        toh(n-1,b,a,c)
toh(1,'a','b','c')