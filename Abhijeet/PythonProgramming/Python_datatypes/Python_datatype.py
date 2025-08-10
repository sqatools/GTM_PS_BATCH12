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

#String follows the indexing
str4 = "Hello"

"""
0 1 2 3 4 +ve
H e l l o
-5 -4 -2 -1 -ve
"""

print(str4[1])
print(str4[-5])
print(str4[-1])
print(str4[1], str4[-4])
print("_"*50)
print('_'*60)
print("""_"""*84)

"""
List data type
List is a mutable data type, we can modify/ update values at any point of time
List contains values in square bracket e.g. [ 6, 8, 4]
List contains all type of data int, float, complex, string, list, tuple, dictionary, set,boolean
List also follows postive, negative indexing like string
Generally we use list data type, where we have dynamic data. e.g. Studnet Registration,
employee management.

"""
list1 = [7, 8.4, 5+7j, 'abc', [1,2,3], (5, 9 ,10), {'a', 84}, {4, 5, 9}, True]
print( list1, type(list1))

"""
indexing
 0  1  2  3 +ve
[5, 7, 8, 4]
-4 -3 -2  -1 -ve
"""
print("_"*50)
print(list1[0])
print(list1[-3])

print("*"*75)

list3 = [5, 7, 9]
list3.append(84)

# Select+Ctrl+Click to view function description
print(list3, type(list3))

print("^"*50)

"""
Tuple is immutable data type, we can not modify/ update Tuple values
Tuple contains values in round brackets
Tuple can contain all data types int, float, complex, string, list, tuple, dict, set, boolean
"""

tuple1 = (7, 8, 4, 1)
print(tuple1, type(tuple1))

tuple2 = (1, 2.84, 5+7j, 'Abhi', [8 ,4, 0, 7], (1,2,3), {'a':84},{6, 9 , 12}, None, True, False)
print(tuple2, type(tuple2))

print("_"*60)
tup3 = (5, 7 , 90)
print(tup3[1])
print(tup3[-2])