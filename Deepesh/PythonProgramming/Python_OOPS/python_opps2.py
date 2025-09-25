"""
class : class is the blueprint of an object where we define all the properties and attribute of the object.
object: object is an entity through which we can access all the properties and attribute define in the class.
method :  When we define any function inside the class, then it becomes method.
          # There are three types of methods.
          1. instance method:  method declare with self as parameter, it is called instance method.
          2. class method:
          3. static method:


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


class XYZ:
    # class variable
    email = "john123@gmail.com"

    def __init__(self, num1, num2):
        self.num1 = num1 # instance variable
        self.num2 = num2 # instance variable

    # instance method
    def multiplication(self):
        print("multiplication :", self.num1 * self.num2)

    @classmethod
    def show_email_id(cls):
        print("Email ID :", cls.email)


    @staticmethod
    def factorial(num):
        """
        ->  static method is associate with class name, no need to create of the class.
        ->  static method is same as like function outside of the class, it can not access
            any of the class member

        :param num:
        :return:
        """
        fact = 1
        for i in range(num ,0, -1):
            fact = fact*i

        print(f"Factorial :{num}", fact)

# access the class method and static method with class name.
XYZ.show_email_id()  # john123@gmail.com
XYZ.factorial(5) # 5 120

# We can not access the instance method with class name
# XYZ.multiplication()
# TypeError: XYZ.multiplication() missing 1 required positional argument: 'self'

obj = XYZ(6, 7)
obj.multiplication()  # multiplication : 42