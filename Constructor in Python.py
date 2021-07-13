# # python constructor-A constructor is a special type of method(fn)which is used to initialize the instance member of the class.
# # in cpp and java the constructor has the same name as class but it treats deifferntlyb in th python.

# # constructor can be of two type:-1.parameterized 2.non-parameterized
# creating the constructor in python : __init__ ()
# non-parameterized constructor--
class Student:
    #constructor-non parameterized
    def __init__(self):
        print("this is a non-parameterized constructor")
    def show(self,name):
        print("Namaste!",name)
student=Student()
student.show("Rahul")


# # parameterized constructor
class Student:
    def __init__(self,name):
        print("this is a parameterized constructor")
        self.name=name
    def show(self):
        print("hello",self.name)
student=Student("Rahul")
student.show()



# default constructor


class Student:
    roll_no=123
    name="Rahul"

    def display(self):
        print(self.roll_no,self.name)
st=Student()
st.display()


# #more than one constructor in the class 
class Student:
    def __init__(self):
        print("the first constructor")
    def __init__(self):
        print('the second constructor')
st=Student()



