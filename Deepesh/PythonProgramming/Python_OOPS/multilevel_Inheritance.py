"""
Inheritance : When one class aquire the property of another class, then it is called inheritance
1. single Inheritance :  class A ->  Class B
2. multi level inheritance :  Class A ->  Class B ->  Class C
3. multiple inheritance :  Class A ->  Class B,  Class C  ->  Class B
4. Hierarchical Inheritance :  Class A ->  Class B, Class A -> Class C

"""


# Multilevel Inheritance

class A:  # Grandfather class
    def __init__(self, A_Var1, A_Var2):
        self.A_Var1 = A_Var1
        self.A_Var2 = A_Var2

    def show_valueof_A_Var1(self):
        print("Value of A Var1 :", self.A_Var1)

    def show_valueof_A_Var2(self):
        print("Value of A Var2 :", self.A_Var2)


class B(A):  # Father class
    """
    When we set up an inheritance between 2 classes, then parent class constructor has to initialize in child
    class constructor
    """
    def __init__(self, B_var1, A_Var1, A_Var2):
        # initialize the parent class constructor with super keyword.
        super().__init__(A_Var1, A_Var2)
        self.B_var1 = B_var1

    def show_value_of_B_Var1(self):
        print("value of B_Var1:", self.B_var1)

    def b_get_all_values(self):
        self.show_valueof_A_Var1()
        self.show_valueof_A_Var2()
        self.show_value_of_B_Var1()


class C(B):
    def __init__(self, C_var1, B_var1, A_Var1, A_Var2):
        super().__init__(B_var1, A_Var1, A_Var2)
        self.C_Var1 = C_var1


    def show_valueof_C_Var1(self):
        print("Value of C_var1:", self.C_Var1)


    def c_get_all_values(self):
        self.show_valueof_A_Var1()
        self.show_valueof_A_Var2()
        self.show_value_of_B_Var1()
        self.show_valueof_C_Var1()



obj = C(100, 200, 300, 400)

obj.show_valueof_C_Var1()
print("_"*50)
obj.c_get_all_values()

"""
Value of C_var1: 100
__________________________________________________
Value of A Var1 : 300
Value of A Var2 : 400
value of B_Var1: 200
Value of C_var1: 100

"""