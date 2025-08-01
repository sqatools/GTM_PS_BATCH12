# Python Data Types:
"""
1. Numbers:
   i). Integer
   ii). Float
   iii). Complex Number

2. Sequential:
   i). String
   ii). List
   iii). Tuple

3. Dictionary
4. Set
5. Boolean
"""

######### Integer ############
"""
Properties:
->  Integer data type if immutable data type.
->  There is not limit for integer data type
->  Integer only contains whole number both +ve and -ve
"""

var1 = 0
var2 = 123
var3 = 789798798789709870987987980798798
var4 = -4534

print(var1, type(var1))
# 0 <class 'int'>

print("_" * 50)
print(var2, type(var2))
# 123 <class 'int'>

print("_" * 50)
print(var3, type(var3))
# 789798798789709870987987980798798 <class 'int'>


print("_" * 50)
print(var4, type(var4))
# -4534 <class 'int'>

print(" Hello " * 5)
#  Hello  Hello  Hello  Hello  Hello


print("_" * 50)
############ Float ############
"""
Properties:
->  Float data type if immutable data type.
->  There is not limit for float data type
->  Float data type only contains pointer number both +ve and -ve
"""

f1 = 0.0
f2 = 0.34
f3 = 89809890.298908
f4 = -56.78

print("f1 :", f1, type(f1))
# f1 : 0.0 <class 'float'>

print("_" * 50)
print("f2 :", f2, type(f2))
# f2 : 0.34 <class 'float'>

print("_" * 50)
print("f3 :", f3, type(f3))
# f3 : 89809890.298908 <class 'float'>

print("_" * 50)
print("f4 :", f4, type(f4))
# f4 : -56.78 <class 'float'>



print("_" * 50)
############ complex ############
"""
Properties:
1.  complex is immutable data type.
2.  complex data type if combination of 2 values, real and imaginary
    e.g.    x+yj,  x= real, y=imaginary
    
3. complex data can +ve and -ve both.
"""

p1 = 10 + 20j
print(p1, type(p1))
print("real value :", p1.real) # real value : 10.0
print("imaginary value :", p1.imag) # imaginary value : 20.0

p2 = -50 -40j
print(p2, type(p2))
# (-50-40j) <class 'complex'>

add_complex_number = p1 + p2
print(add_complex_number)
# (-40-20j)



print("_" * 50)
############ String ############