"""
Inheritance : When one class aquire the property of another class, then it is called inheritance
1. single Inheritance :  class A ->  Class B
2. multi level inheritance :  Class A ->  Class B ->  Class C
3. multiple inheritance :  Class A ->  Class B,  Class C  ->  Class B
4. Hierarchical Inheritance :  Class A ->  Class B, Class A -> Class C

"""


# Single Inheritance

class A:  # Father
    def __init__(self, A_Var1, A_Var2):
        self.A_Var1 = A_Var1
        self.A_Var2 = A_Var2

    def show_valueof_A_Var1(self):
        print("Value of A Var1 :", self.A_Var1)

    def show_valueof_A_Var2(self):
        print("Value of A Var2 :", self.A_Var2)


class B(A):  # Son
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

    def get_all_values(self):
        self.show_valueof_A_Var1()
        self.show_valueof_A_Var2()
        self.show_value_of_B_Var1()


obj = B(50, 60, 70)
obj.show_value_of_B_Var1()

print("_" * 50)
obj.get_all_values()
