# Session-2
# python data types
"""
1.Number
  *Integer
  *Float
  *complex number
2.Sequential
  *String
  *list
  *Tuple
3.Dictionary
# 4.Set
# 5.Boolean
import string
import time

# * Integer properties:
# / Integer data type if immutable data types
# / there is no limit for integers data types
# / Integer only contains whole numbers both +ve and -ve
"""
from typing import List, Any

var1 = 0
var2 = 123
var3 = 987456799456
var4 = -4534
print(var1, type(var1))
# 0 <class 'int'>
print(var2, type(var2))
# 123 <class 'int'>
print(var3, type(var3))
# 987456799456 <class 'int'>
print(var4, type(var4))
# -4534 <class 'int'>

print("_" * 50)
# *Float properties
"""
# / Float data type if immutable data types
# / there is no limit for float data types
# / Float only contains pointer numbers both +ve and -ve
"""
f1 = 0.0
f2 = 0.34
f3 = 7894.56123
f4 = -582369
print("f1:", f1, type(f1))
# f1: 0.0 <class 'float'>
print("_" * 50)
print("f2:", f2, type(f2))
# f2: 0.34 <class 'float'>
print("_" * 50)
print(f3, type(f3))
# 7894.56123 <class 'float'>
print("f3:", f3, type(f3))
# f3: 7894.56123 <class 'float'>
print("_" * 50)
print("f4:", f4, type(f4))
# f4: -582369 <class 'int'>

print("_" * 50)
# * Complex numbers properties
"""
/ comples is immutable data types
/ complex data type if combination of 2values real and imaginary
   eg: x+yj, x=real y=imaginary
/ complex data can +ve and -ve both
"""
p1 = 10 + 20j
print(p1, type(p1))
# (10+20j) <class 'complex'>
print("real value:", p1.real)
# real value: 10.0
print("imaginary value:", p1.imag)
# imaginary value: 20.0
print("_" * 50)
p2 = -50 - 40j
print(p2, type(p2))
# (-50-40j) <class 'complex'>

add_complex_number = p1 + p2
print(add_complex_number)
# (-40-20j)
print("_" * 50)

# Session-2
################ 2.Sequential ############
# *String
"""
Properties
->String is a immutable data type
->we can define with single/double/triple quotes.
->String follows postive and negative indexing
->String can contains any type of data as raw string.
"""
s1 = ''
s2 = "hello good moring"
s3 = """
  Thank you, India and England . THis was a Test series of the highest order.
this was the Ali VS Foreman of cricket. a battle where two heavy weight went blow for blow to make
the whole world rumble with excitment. A battle where after 25 days of hard cricket we still had no outright
victories just two champion teams in this own right who have given the red ball some reverence one again in this
age of T20 extravagance. What can say but thankyou.
"""
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

str4 = "hello"
# "0 1 2 3 4
#  h e l l o
# -5-4-3-2-1"
print(str4[0])
print(str4[-5])
print(str4[3], str4[-2])
print("_" * 50)

#################### List ###############
"""properties
->List is mutable data type, we can modify/update list values at any point of time.
-> list contain values in square bracket Eg: [6,8,7]
->list can contian all types of data types int, float,string, list,tuple,dictionary, set,boolean, complex
->list also follows +ve and -ve indexing as like string.
->Generally we usee list data type, wher we have dynamic data,
    Eg:Student registration
     employee management.
"""
list1 = [3, 45, 5 + 7j, 'hello', [7, 8, 9], (2, 5, 8), {'a': 123}, {4, 5, 6}]
print(list1, type(list1))
list2 = [5, 7, 9, 3]
#  0 1 2 3
#  5 7 9 3
# -4-3-2-1
print(list2[1])
print(list2[-3])
print(list2[2], list2[-2])

list3 = [6, 7, 9]
list3.append(100)
print(list3, type(list3))
print("_" * 50)
"""
####################### Tuple ####################
  properties
->Tuple is immutable data type, we can modify/update tuple
-> tuple contains values in square bracket eg:(1,2,2)
->tuple can contain all type of data, int, float, complex,string, list,tuple,dictionary , set,boolean
-> tuple also follows +ve and -ve indexing as like string and list
->generally we use tuple data type, where we have fixed data.
eg:months in year
   days in week
"""

tup1 = (3, 6, 9, 1)
print(tup1, type(tup1))

tup2 = (3, 5.6, 'python', [5, 8, 7], (7, 8, 2), {'a': 123}, {6, 7, 8}, True, False, None)
print(tup2, type(tup2))

tup3 = (8, 7, 9, 55)
print(tup3[2])
print(tup3[-2])
print(tup2[3])
print("_" * 50)
# session-3
############## Dictionary #######################
"""
->dict is mutable data type, that we can modify any point of time
->dict store data in key:value formate with curly braces eg:{'a':123}
->dict only contains uniques keys,
 duplicate keys are not allowed,
 if we define any duplicate key, then it will consider the lastest define value
 ->only immutable data type can be key in the dict eg:int,float, complex,string, tuple,boolean,
 -> there is restriction of value data in the dict. all type of data can be value in dict.
 ->dict store data in LTFO(LAST IN FIRST OUT) algo.
 ->dict does not follow indexing.
 ->dict does not follow indexing.
 """
dict1 = {'name': 'rahul', 'age': 25, 'address': 'mumbai', 'phone': 78945612237, 'email': 'rahul@gmail'}
print(dict1, type(dict1))
# {'name': 'rahul', 'age': 25, 'address': 'mumbai', 'phone': 78945612237, 'email': 'rahul@gmail'} <class 'dict'>

print("name:", dict1['name'])  # name: rahul
print("age:", dict1['age'])  # age: 25

dict1={'name':'rahul', 'age':25, 'address':'mumbai, borwali', 'phone':7894561234, 'email':'rahul@gmail.com'}
dict1['county']="india"
print(dict1)
#{'name': 'rahul', 'age': 25, 'address': 'mumbai, borwali', 'phone': 7894561234, 'email': 'rahul@gmail.com', 'county': 'india'}

#dict only contain unique keys, duplication keys are not allowed.
#if we define any duplicate key, then it will consider the latest define value
dict2={'a':123,'b':567,'c':741,'a':777}
print(dict2)  #{'a': 777, 'b': 567, 'c': 741}

#only immutable data type can be key in the dict eg:int,float,complex,tuple,boolean.
dict3={
    5:56,
    5.77: 'hello',
    50+30j: [50,60,70],
    'python': (2,4,7),
    (1,2,3): {'a':123, 'b':456},
    True: {4,5,6,7},
    # #TypeError: unhashable type: 'list'
    #ograming', #TypeError: unhashable type: 'dict'
    #{5,5,6,8}: 900  #TypeError: unhashable type: 'set'
}
print("dict3:", dict3)
#dict3: {5: 56, 5.77: 'hello', (50+30j): [50, 60, 70], 'python': (2, 4, 7), (1, 2, 3): {'a': 123, 'b': 456}, True: {4, 5, 6, 7}}

print("_"*50)
user_info=['rahul','rahul@gmail.com',7894561235,'mumbai']
print(user_info[1])  #rahul@gmail.com

user_info_dict={'name':'rahul','city':'mumbai','phone':7894561235,'email':'rahul@gmail.com'}
print(user_info_dict['email'])  #rahul@gmail.com

batch12={
    'str1':{'name':'rakshi','age':22,'city':'kolar','phone':7894561231},
    'str2':{'name':'uma','age':24,'city':'bangalore','phone':774158251},
    'str3':{'name':'pradeep','age':28,'city':'mumbai','phone':7418529631},
}
print(batch12['str3'])
print(batch12['str2']['phone'])
#{'name': 'pradeep', 'age': 28, 'city': 'mumbai', 'phone': 7418529631}
774158251
print("_"*50)
##################### set ################
set1={5,6,7,4,8,6,9}
print(set1, type(set1))
#{4, 5, 6, 7, 8, 9} <class 'set'>

#set is mutable dat type, we can modify the data at point of time
set2={7,2,3,5,8,}
set2.add(40)
print(set2,type(set2))
#{2, 3, 5, 7, 8, 40} <class 'set'>

set2.add(100)
print(set2, type(set2))
#{2, 3, 100, 5, 7, 8, 40} <class 'set'>

#set only contain immutable data type as set member Eg: int,float,complex,string,tuple,boolean
set3={5,6.4, 'python', 40+50j, (5,2,8), True}
print("set:", set3)
#set: {True, 5, 'python', 6.4, (5, 2, 8), (40+50j)}

set4={5,7.6,40+58j,'python',True,}
print("set4", set4)
[7,8,9] #TypeError: unhashable type: 'list'
{4,5,6} #TypeError: unhashable type: 'set'
{'a':123} #TypeError: unhashable type: 'dict'
print("_"*50)

############## Boolean #############
var1=True
var2=False
print(var1, type(var1))
print(var2, type(var2))
#True <class 'bool'>
#False <class 'bool'>
a=50
b=60
c=50
print(a==b) #False
print(a==c) #True









































