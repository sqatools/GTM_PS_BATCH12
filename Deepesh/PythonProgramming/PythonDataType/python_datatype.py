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
print("real value :", p1.real)  # real value : 10.0
print("imaginary value :", p1.imag)  # imaginary value : 20.0

p2 = -50 - 40j
print(p2, type(p2))
# (-50-40j) <class 'complex'>

add_complex_number = p1 + p2
print(add_complex_number)
# (-40-20j)


print("_" * 50)
############ String ############
"""
# Properties:
->  string is immutable data type.
->  we can define string with single/double/triple quotes.
->  string follows positive and negative indexing.
->  string can contains any type of data as raw string.
"""

s1 = ''
s2 = "Hello good morning"
s3 = """
Thank you, India and England. This was a Test series of the highest order. 
This was the Ali vs Foreman of cricket - a battle where two heavyweights 
went blow for blow to make the whole world rumble with excitement. 
A battle where after 25 days of hard, grueling cricket we still had 
no outright victors. Just two champion teams in their own right who 
have given the red ball some reverence once again in this age of T20 extravagance.
What can we say but thank you
"""

print(s1, type(s1))  # <class 'str'>

print("_" * 50)
print(s2, type(s2))
# Hello good morning <class 'str'>

print("_" * 50)
print(s3, type(s3))
"""
Thank you, India and England. This was a Test series of the highest order. 
This was the Ali vs Foreman of cricket - a battle where two heavyweights 
went blow for blow to make the whole world rumble with excitement. 
A battle where after 25 days of hard, grueling cricket we still had 
no outright victors. Just two champion teams in their own right who 
have given the red ball some reverence once again in this age of T20 extravagance.
What can we say but thank you
 <class 'str'>
"""

# string follows the indexing
str4 = "Hello"

"""
 0  1   2   3   4  +ve
 H  e   l   l   o
-5 -4  -3  -2  -1  -ve
"""

print(str4[0])  # H +ve
print(str4[-5])  # H -ve

print(str4[3], str4[-2])  # l l

print("_" * 50)
################## List #################
"""
Properties:
->  List is mutable data type, we can modify/update list values at any point of time.
->  List contains values in square bracket. e.g  [6, 8, 3]
->  List can contain all types of data, int, float, complex, string, list, tuple, dictionary, set, boolean
->  List also follows +ve and -ve indexing as like string.
->  Generally we use list data type, where we have dynamic data, e.g. 
    student registration, 
    employee management.
"""

list1 = [3, 4.5, 5 + 7j, 'Hello', [7, 8, 3], (2, 5, 8), {'a': 123}, {4, 6, 7}, True]

print(list1, type(list1))
# [3, 4.5, (5+7j), 'Hello', [7, 8, 3], (2, 5, 8), {'a': 123}, {4, 6, 7}, True] <class 'list'>


list2 = [5, 7, 9, 3]

"""
 0   1    2      3   +ve
[5,  7,   9,     3]
-4   -3   -2    -1   -ve
"""

print(list2[1])  # 7
print(list2[-3])  # 7

list3 = [6, 7, 9]
list3.append(100)
print(list3, type(list3))
# [6, 7, 9, 100] <class 'list'>
list3.insert(0, 700)
print(list3, type(list3))
# [700, 6, 7, 9, 100] <class 'list'>


print("_" * 50)
################## Tuple #################
"""
Properties:
->  Tuple is immutable data type, we can not modify/update Tuple values.
->  Tuple contains values in square bracket. e.g  (6, 8, 3)
->  Tuple can contain all types of data, int, float, complex, string, list, tuple, dictionary, set, boolean
->  Tuple also follows +ve and -ve indexing as like string and list
->  Generally we use Tuple data type, where we have fixed data, \
    e.g. Months in year, days in week. 
"""

tup1 = (3, 6, 8, 1)
print(tup1, type(tup1))
# (3, 6, 8, 1) <class 'tuple'>

tup2 = (3, 5.6, 'Python', [4, 6, 7], (1, 6, 2), {'a': 12}, {6, 7, 2}, True, False, None)
print(tup2, type(tup2))

# (3, 5.6, 'Python', [4, 6, 7], (1, 6, 2), {'a': 12}, {2, 6, 7}, True, False, None) <class 'tuple'>

tup3 = (5, 7, 99)
print(tup3[2])  # 99
print(tup3[-2])  # 7

print(tup2[4])  # (1, 6, 2)
print(tup2[-4])  # {2, 6, 7}

var1 = "uma"
var2 = "devi"
var3 = var1 + var2
print(var3)

print("_" * 50)
############################### Dictionary Data Type ######################
"""
# Properties:
->  dict is mutable datatype, that we can modify any point of time.
->  dict store data in key:value format with curly braces e.g  {'a': 123}
->   dict only contains uniques keys, duplicate keys are not allowed.
    if we define any duplicate key, then it consider the latest define value
->  Only immutable data type can be key in the dict. e.g int, float, complex, string, tuple, boolean.
->  There is restriction of value data in the dict. all type of data can be value in dict.
->  Dict store data in LIFO ( LAST IN FIRST OUT ) format.   
->  Dict does not follow indexing.
"""

dict1 = {'name': 'Rahul', 'age': 25, 'address': 'Mumbai, boriwali', 'phone': 7897987987, 'email': 'rahul@gmail.com'}
print(dict1, type(dict1))
# {'name': 'Rahul', 'age': 25, 'address': 'Mumbai', 'phone': 7897987987, 'email': 'rahul@gmail.com'} <class 'dict'>

print("Name :", dict1['name'])
# Name : Rahul
print("Age :", dict1['age'])
# Age : 25

# dict is mutable datatype, that we can modify any point of time.
dict1['country'] = "India"
print(dict1)

# 'name': 'Rahul', 'age': 25, 'address': 'Mumbai, boriwali', 'phone': 7897987987, 'email': 'rahul@gmail.com', 'country': 'India'}


print("_" * 50)
# dict only contains uniques keys, duplicate keys are not allowed.
#     if we define any duplicate key, then it will consider the latest define value

dict2 = {'a': 123, 'b': 567, 'c': 789, 'a': 777}
print(dict2)
# {'a': 777, 'b': 567, 'c': 789}

print("_" * 50)
###############################
# Only immutable data type can be key in the dict. e.g int, float, complex, string, tuple, boolean.

dict3 = {
    5: 5.6,
    5.77: 'Hello',
    50 + 30j: [50, 60, 70],
    'Python': (2, 4, 7),
    (1, 2, 3): {'a': 123, 'b': 456},
    True: {4, 5, 7, 12},
    # [4, 7, 8] : 678            # TypeError: unhashable type: 'list'
    # {'a': 34} : 'Programming'  # TypeError: unhashable type: 'dict'
    # {5, 7, 3} : 900            # TypeError: unhashable type: 'set'
}

print("dict3 :", dict3)

print("_" * 50)

user_info = ['rahul', 'rahul@gmail.com', 787987987, 'mumbai']
print(user_info[1])

user_info_dict = {'name': 'rahul', 'city': 'mumbai', 'phone': 734673456, 'email': 'rahul@gmail.com'}
print(user_info_dict['email'])

batch12 = {
    'st1': {'name': 'pradeep', 'age': 34, 'city': 'mumbai', 'phone': 5678935643},
    'st2': {'name': 'sourabh', 'age': 30, 'city': 'pune', 'phone': 5463453645},
    'st3': {'name': 'umadevi', 'age': 38, 'city': 'Bangalore', 'phone': 5654654634},
    'st4': {'name': 'itishree', 'age': 23, 'city': 'Chennai', 'phone': 788768787},
}

print(batch12['st4']['phone'])
# 788768787


print("_" * 50)
##################################### Set data type ###################################
set1 = {5, 3, 2, 1, 7, 2, 5, 7, 8, 9}
print(set1, type(set1))
# {1, 2, 3, 5, 7, 8, 9} <class 'set'>

"""
# Properties:
->  Set is mutable data type, we can modify the data at point of time.
->  Set contains data in curly braces, {}
->  Set store values in random order.
->  Set only store unique values, it means duplicate values are not allowed.
    if try to add same values multiple times, it will consider the one time only.
->  Set only contains immutable data type as set member. e.g int, float, complex, string, tuple, boolean.
"""

#  Set is mutable data type, we can modify the data at point of time.
set2 = {5, 7, 9}
set2.add(50)
print(set2, type(set2))
# {9, 50, 5, 7}
set2.add(9)
print(set2, type(set2))

print("_" * 50)
#  Set only contains immutable data type as set member. e.g int, float, complex, string, tuple, boolean.
set3 = {5, 7.8, 40 + 50j, 'Python', (3, 5, 7), True}
print("set3 :", set3)

# set4 = {5, 7.8, 40+50j, 'Python', (3, 5, 7), True, {'A': 123}}
# print("set4 :", set4)
# TypeError: unhashable type: 'list'
# TypeError: unhashable type: 'set'
# TypeError: unhashable type: 'dict'


print("_" * 50)
##################################### Boolean datatype ###################################
"""
Properties:
->  Boolean is immutable data type.
->  Boolean data type only contains two values True or False
->  Boolean data is output of any specific condition of program
"""

var1 = True
var2 = False
print(var1, type(var1))  # True <class 'bool'>
print(var2, type(var2))  # False <class 'bool'>

a = 50
b = 70
c = 50
print(a == b)  # False
print(a == c)  # True
