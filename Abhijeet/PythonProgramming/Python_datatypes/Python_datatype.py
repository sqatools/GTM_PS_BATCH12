"""
Python Data types

1. Numbers
i.Integer
ii.Float
iii.Complex number

2.Squential:
i.String
ii.List
iii.Tuple

3. Dictionary
4.Set
5.Boolean
"""
from Deepesh.PythonProgramming.PythonDataType.python_datatype import add_complex_number

####Integer####
"""Properties:
->It is immutable
->There is no limit for intger value
->Contains only whole number +ve -ve

"""
var1 = 0
var2 = 84
var3 = 2353246754783486586
var4 = -539

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))

print('_'*50)
"""
Properties
-Float data type is immutable data type
-There is no limit for float data type length
-Float data type contains pointer number both +ve and -ve
"""
f1 = 0.0
f2 = 0.34
f3 = 85.84
f4 = -90
print("f1 :",f1,type(f1))
print("_"*50)
print("f2:",f2,type(f2))
print(("_"*50))
print("f3 :", f3, type(f3))
print("f4 :", f4, type(f4))

print('_'*50)

"""
1. Complex is immutable data type
2. Complex data type is combination of 2 real values, real and imaginary
    e.g. x+yj, x=real, y=imaginary
3. Complex data can be both +ve and _ve
"""
p1 = 10 +25j
print('p1 :', p1, type(p1))
print("real value:", p1.real)
print("imaginary value", p1.imag)
print('_'*50)
p2 = -50 -40j
print(p2, type(p2))
add_complex_number = p1+p2
print(add_complex_number)

print('_'*50)

"""
-String is immutable data type
-we can define string with single/ double/ triple quotes
-String follows positive and negative indexing
-String can contain any type of data as raw string
"""
s1 = ''
s2 = "String with double quotes"
s3 = '''Automation testing
Python
Playwright
'''

print(s1, type(s1))
print(s2, type(s2))
print(s3), type(s3)