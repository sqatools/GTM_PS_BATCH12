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

print("%"*50)
"""
Dictionary is a mutable data type which we can update at any point
Dictionary store data in key:value format with curly braces e.g. {'a':5}
Dictionary contains only unique keys
If we define any dupliate keys, then it consider the latest value
Only immutable data types can be key in dictionary 
i.e. int, float, complex, string, tuple, boolean
There is no restriction on value of data in dict. All type of data can be value in dictionary
Dictionary store data in LIFO ( Last in first out) algo
Dictionary does not follow indexing
"""
dict1 = { "Name": "Abhijeet", "Age": 40, "Address": "Pune", "Phone": 7777777778, "Email": "test@test.com"}
print(dict1, type(dict1))
print(dict1["Name"])
#Dictionary is mutable data type that we can modify any point of time
dict1["Country"] = "India"
print(dict1)
dict1["State"] = "Maharashtra"
print(dict1)
print("+"*50)
#Dictionary contains only unique keys. Duplicate keys are not allowed
#If we define any duplicate key, then it will consider only latest defined value
dict2 = {"a":123, "b":577, 'c':786, 'a':777}
print(dict2)
print("="*50)
#Only immutable data types can be key in Dict
dict3 = {
    5: 5.6,
    5.77:'Hello',
    50+30j:[50,60,70],
    'Python':(2,4,7),
    (1,2,3): {"a":123, 'b': 456},
    True :{4, 5, 7, 12},
    #[1,2]:1
}
print(dict3)

print("$"*100)

batch12 = {
'st1' : {'name': 'Pradeep', 'Age':34, 'City':'Mumbai', 'Phone':234325456},
'st2' : {'name': 'Sourav', 'Age':30, 'City':'Mumbai', 'Phone':234325456},
'st3' : {'name': 'Umadevi', 'Age':38, 'City':'Mumbai', 'Phone':234325456},
'st4' : {'name': 'Itishree', 'Age':23, 'City':'Mumbai', 'Phone':234325456}
}

print(batch12['st4']['Phone'])
print("_"*50)
######Set##########################################
"""
Set is mutable data type, modify data at any point of time

"""
set2 = {5,7,9}
set2.add(5)
print(set2, type(set2))

print("+"*50)

###########################SET###################################
"""
Set is a mutable data type, we can modify data at any point of time
It contains data in curly braces {}
Set store values in random order
Set only store unique values, it means duplicate values are not allowed
If we try to add same values multiple times, it will consider it one time only
Set only contains immutable data types Int, Float, Complex, String, Tuple, Boolean
Set, list, and dictionary are mutable so set can not contain thse vakues


"""

set2 = {5 ,7, 9}
set2.add(50)
print(set2, type(set2))
set3 = {5, 7.8, 40+50j, 'Python', (3,5,7), True}
print(set3, type(set3))

print("**"*50)

"""
Boolean is immutable data type
Boolean data type only contains two values True or False
Boolean data is output of specific condition of program
"""
var1 = True
var2 = False
print(var1, type(var1))
print(var2, type(var2))

a = 50
b = 70
c = 50
print(a==c)
print(b==c)
print(a==c)