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

print("_"*50)
print(s2, type(s2))
# Hello good morning <class 'str'>

print("_"*50)
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

print(str4[0])   # H +ve
print(str4[-5])  # H -ve

print(str4[3], str4[-2]) # l l

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

list1 = [3, 4.5, 5+7j,  'Hello', [7, 8, 3], (2, 5, 8), {'a': 123}, {4, 6, 7}, True]

print(list1, type(list1))
# [3, 4.5, (5+7j), 'Hello', [7, 8, 3], (2, 5, 8), {'a': 123}, {4, 6, 7}, True] <class 'list'>


list2 = [5, 7, 9, 3]

"""
 0   1    2      3   +ve
[5,  7,   9,     3]
-4   -3   -2    -1   -ve
"""

print(list2[1])  # 7
print(list2[-3]) # 7


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
print(tup3[-2]) # 7

print(tup2[4])  # (1, 6, 2)
print(tup2[-4]) # {2, 6, 7}