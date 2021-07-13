def myfun():#recursion
    print("geekyshows")
    myfun()
myfun()



i=0
def myfun():
    global i
    i=i+1
    print("my function",i)
    myfun()
myfun()


i=0
def myfun():
   i=0
   i=1


    i=i+1
    print("my function",i)
    myfun()
# myfun()
import sys
print(sys.getrecursionlimit())



