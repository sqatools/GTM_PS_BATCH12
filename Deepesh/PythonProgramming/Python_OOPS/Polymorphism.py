"""
1. method overriding:  When parent class and child class have same method with different behavior,then child class override parent class method.
                       this concept is known as method overriding.

2. method overloading :  Python does not support method overloading.
                      ->  When one class has 2 method with same name and different params, then it is called method overloading.
                      ->  When
3. operator overloading
"""


class Company:
    def __init__(self, comp_name, comp_address):
        self.comp_name = comp_name
        self.comp_Address = comp_address


    def show_company_name(self):
        print("name of company :", self.comp_name)


    def show_address(self):
        print("The company address is :", self.comp_Address)



class ShowRooms(Company):
    def __init__(self, showroom_name, showroom_address, comp_name, comp_address):
        super().__init__(comp_name, comp_address)
        self.showroom_name = showroom_name
        self.showroom_address = showroom_address


    def show_showroom_name(self):
        print("Showroom name :", self.showroom_name)


    def show_address(self):
        print("The Showroom address is:", self.showroom_address)


    def addition(self, n1, n2):
        print("addition of n1 , n2:", n1+n2)


    def addition(self, v1, v2, v3):
        print("Addition of v1, v2, v3 :", v1+v2+v3)



obj = ShowRooms("Bhagirath TATA", "Pune , Hinjewadi", "TATA", "Mumbai Headoffice")
obj.show_address()
# The Showroom address is: Pune , Hinjewadi


obj.addition(40, 50, 60)
# Addition of v1, v2, v3 : 150


################################# operator overloading ############
# for each operator python has magic method with each data type, that overload the opertor
# Examples given below.
v1 = 40
v2 = 50
print(v1+v2)
print(v1.__add__(v2))
print(dir(int))


s1 = "Hello"
s2 = "Programming"
print(s1+s2)
print(s1.__add__(s2))
print(dir(str))


