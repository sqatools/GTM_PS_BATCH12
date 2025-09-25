"""
class : class is the blueprint of an object where we define all the properties and attribute of the object.
object: object is an entity through which we can access all the properties and attribute define in the class.
method :  When we define any function inside the class, then it becomes method.
constructor :  constructor initialize the memory of object when we initiate it.
               ->  constructor being called, whenever we create object of the class
               def __init__():
                    code

               1.  default constructor:  when we don't provide any parameter to the constructor, then it is default constructor
               2.  parametrize constructor :  when define parameter to the constructor, then it is called parametrized constructor.

variables :  There are two types of variable
             1. instance variable :  any variable we declare with self is called instance variable, we can access all the variables across the class.
             2. class variable :  any variable we declare on class level, then it is called class variable

"""


class ABC:
    # class variable
    phone = 7897987879

    def __init__(self, n1, n2):
        print("-----Object creation successful---")
        self.var1 = n1  # instance variable
        self.var2 = n2  # instance variable

    # instance Method
    def greeting(self):
        print("Welcome to OOPS learning")

    # instance Method
    def square(self, n):
        print(f"sqaure of {n}:", n ** 2)

    # instance Method
    def addition(self):
        print(f"Addition of {self.var1}, {self.var2}: {self.var1 + self.var2}")


# create object of the class
obj = ABC(50, 40)
print(obj)  # <__main__.ABC object at 0x000001D265C77230>

# call method with class object
obj.greeting()  # Welcome to OOPS learning

# call square method with object
obj.square(5)  # sqaure of 5: 25

print(type(obj))  # <class '__main__.ABC'>

var1 = "Hello"
print(type(var1))  # <class 'str'>

# call addition method with instance variable
obj.addition()  # Addition of 50, 40: 90


# access the class variables outside of the class
print(obj.phone)  # 7897987879

# change variable value with object
obj.var1 = 100
obj.var2 = 300
obj.addition() # Addition of 100, 300: 400

# update class variable
obj.phone = 8898989899
print("Phone number :", obj.phone) # Phone number : 8898989899