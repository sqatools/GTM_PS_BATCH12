"""
Inheritance : When one class aquire the property of another class, then it is called inheritance
1. single Inheritance :  class A ->  Class B
2. multi level inheritance :  Class A ->  Class B ->  Class C
3. multiple inheritance :  Class A ->  Class B,  Class C  ->  Class B
4. Hierarchical Inheritance :  Class A ->  Class B, Class A -> Class C

"""


# Single Inheritance

class Father:  # Father
    def __init__(self, f_name, f_business, f_car):
        self.f_name = f_name
        self.f_business = f_business
        self.f_car = f_car

    def show_father_details(self):
        print("Father name :", self.f_name)
        print("Father Business :", self.f_business)
        print("Father car :", self.f_car)


class Mother:
    def __init__(self, m_name, m_business):
        self.m_name = m_name
        self.m_business = m_business

    def show_Mother_details(self):
        print("Mother name :", self.m_name)
        print("Mother Business :", self.m_business)


# MRO : Method Resolution Order
# The order of class being called while setting up the inheritance between 2 classes will get, will decide the priority of the
# constructor to be initialized in child class constructor.
class Son(Mother, Father):
    def __init__(self, s_name, m_name, m_business, f_name, f_business, f_car):
        super().__init__(m_name, m_business)
        self.s_name = s_name
        self.f_name = f_name
        self.f_business = f_business
        self.f_car = f_car



    def show_complete_family_details(self):
        self.show_father_details()
        self.show_Mother_details()
        print("Name of son :", self.s_name)



obj = Son("Rahul", "Mrs Pooja", "Fashion", "Mr Mohan", "Construction", "BMW")
obj.show_Mother_details()
print("_"*40)
obj.show_father_details()
print("_"*50)
obj.show_complete_family_details()
