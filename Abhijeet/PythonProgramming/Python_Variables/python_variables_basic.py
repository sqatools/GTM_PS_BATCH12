from Deepesh.PythonProgramming.Python_Variables.python_variables_basic import output

a=10
# a Variable
# = assignment
# 10 is value to assign to variable

print(a,id(a))
print("_"*50)
# if multiple variables have same value, address will be same

p= 50
q = 50

print(p,id(p))
print(q,id(q))

print("_"*50)

# Assign single value to multiple variables
x = y = z = 100
print("Value of x :", x)
print("value of y :", y)
print("Value of z :", z)

print("_"*50)
# Assign different values to diff variables
A, B, C = 85, 84, 83
print("Value of A :", A)
print("Value of B :", B)
print("Value of C :", C)
print(A,B,C)

print("_"*50)
# Rule to define variable

#There should not be space in variable name
# var a = 500 invalid
a = 500 # valid

#There is no limit for variable name length
var_can_be_of_any_length = 84
#Variable name can not start with Number
# 55variable = 100 Invalid
variable55 = 100 # Valid
#Variable name should not contain special character except '_' underscore

#variable&new = 100 Invalid
variable_new = 100 # Valid

#Variable names are case sensitive
name = 'Abhijeet'
NAME = 'Abhi'
Name = 'Abhis'
nAme = 'Abhishro'

print(name,"|", Name, "|", nAme,"|",NAME)

print("_"*50)

####################
"""
Mathematical Operators
+ : Addition
- : Subtraction
* : Multiplication
/ : Division with fraction
//:Division without fraction
% :Remainder operator
== : equal to 
!= : Not equal to
** : Power operator
"""
var1 = 50
var2= 6
print("Addition :", var1+var2)
output = var1+var2
print("Output :", output)
print("Subtraction:", var1-var2)
print("Multiplication :", var1*var2)
print("Division with single / :", var1/var2)
print("Division with // :", var1//var2)
print("Remainder % :", var1%var2)
# compare two values
P = 200
Q = 300
R = 200
print(P==Q)
print(P==R)
print(Q==R)
print(P!=R)
# Get power of value
print("Square of 5:", 5**2)
print("Cube of 5 :", 5**3)

print("_"*50)

#Solve the equation
#(a+b)^2 = a^2 +b^2+ 2ab
a = 5
b = 7
LHS = (a+b)**2
RHS = a**2 + b**2 + 2*a*b
print(LHS == RHS)