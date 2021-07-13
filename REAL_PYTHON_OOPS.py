# class Dog:
#     species="jnjsnjal" #class attribute
#     def __init__(self,name,age,sound):#constructor
#         self.name=name
#         self.age=age
#         self.sound=sound
# #Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old."
# #another instance method
#     def speak(self):
#         return f"{self.name}says {self.sound}"
# rocky=Dog(name='rocky',age=4,sound='bow wow')
# annie=Dog(name='annie',age=5,sound='lalla')
# print(rocky.name)
# print(rocky.age)
# print(rocky.sound)
# print(annie.name)
# print(annie.sound)
# print(rocky.description())
# print(rocky.sound)
# print(rocky.speak())
# print(annie.description())
# print(annie.speak())

# print(rocky.species)




class Car:
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
    def price_inc(self):
        self.price= int(self.price*1.5)


honda=Car("city",2017,1000000)
tata=Car('indica',2015,600000)
# print(honda.modelname)
# print(honda.yearm)
# print(honda.price)
# print(tata.modelname)
# print(tata.yearm)
# print(tata.price)
# print(honda.__dict__)
# print(tata.__dict__)
# honda.cc=1500
# print(honda.cc)
# print(honda.__dict__)
# honda.owner='rahul'
# print(honda.__dict__)
print(honda.price)
honda.price_inc()
print(honda.price)