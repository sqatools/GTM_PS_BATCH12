a = 10
# a :  variable
# = :  assignment
# 10 : value to assign variable
print(a, id(a))
# 10 140717031900360

a = 11
print(a, id(a))
# 11 140717031900392

a = 10
print(a, id(a))
# 10 140717031900360


print("_"*50)
### if multiple variable have same values, then their address is also same ###
p = 50
q = 50
print("p:", p, ":", id(p))  #50 : 140718301792712
print("q :", q, ":", id(q)) # 50 : 140718301792712


print("_"*50)
### Assign single value to multiple variable ###
x = y = z = 100
print("value of x :", x) # value of x : 100
print("value of y :", y) # value of y : 100
print("value of z :", z) # value of z : 100


print("_"*50)
### Assign different values to different variables ###
A, B, C = 50, 100, 200
print("value of A :", A)  # value of A : 50
print("value of B :", B)  # value of B : 100
print("value of C :", C)  # value of C : 200
print(A, B, C)  # 50 100 200

##################################
# Rules to define variable name

# 1. There should not be space in variable name.
# var a= 500 : invalid
var_a = 500 # valid

# 2. There is no limit for variable name length.
w = 10  # valid
hello_we_Are_learning_Python_programming = 500 # valid

# 3. Variable name can not start with number.
# 123_var = 700  : invalid
var_123 = 800 # valid

# 4. Variable name should not contain special characters in the name except _
# var&123 = 600 # invalid
# var*abc = 700 # invalid

# 5. variable names are case-sensitive.

name = 'Rahul'
Name = 'Manoj'
NAME = 'Mohit'
NAme =  'John'
namE =  'Raghav'

print(name, "|", Name, "|", NAME, "|", NAme, "|", namE)
# Rahul | Manoj | Mohit | John | Raghav


print("_"*50)
###############################
"""
Mathematical Operators
 + :  plus
 - : minus
 * : multiply
 / : division with single /
 // :  division with double //
 % :  remainder operator
 == :  equal to operator
 != :  not equal to operator
 ** : power operator
"""
var1 = 50
var2 = 6
print("Addition :", var1 + var2)
output = var1 + var2
print("output :", output)
print("subtraction :", var1 - var2) # 44
print("Multiplication :", var1*var2) # 300
print("Division with / :", 15/2) # 7.5
print("Division with //:", var1//3) # 16
print("Remainder value :", 15%4) #  3

# compare two value
P = 300
Q = 500
R = 300
print(P == Q) # False
print(P == R) # True
print(Q != R) # True

# get power of value
print("square of 5 :", 5**2) # 25
print("Cube of 12 :", 12**3) # 1728

print("_"*40)
########################################## #
# try to this equation
# (a+b)^2 = a^2 + b^2 + 2ab

a = 5
b = 6
LHS = (a+b)**2
RHS = a**2 + b**2 + 2*a*b
print(LHS == RHS) # True

# https://sqatools.in/python-basic-programs/
# solve atleast 10 programs from this


# Home work
"""
# (a+b)*(a-b) = a^2 - b^2
# (a+b)^3 = a^3 + b^3 + 3ab(a+b)
# calculate simple interest
A = P(1+rt)
P = Principle
r = rate of interest
t = time in years

# calculate compound interest

A = P (1+r/n)^nt
r = rate of interest
t = time in year
P = Principle
n = number of times interest applied the time period
# 

# Pythgorous Theorem
# a2  = b2 + c2


"""