# augest 6 2025

# Integer to float

a = 4
# f1 = float >> keyword called float
f1 = float(a)
print(f1, type(f1))

# int>string

w = 4567
s1 = str(w)
s1 = str(4567)
print("value:", s1)

# assigning the int value to string
print(s1, type(s1))
print(s1)

# Int> list  we cannot 'int' object is not iterable
# Int> tuple  we cannot 'int' object is not iterable
# Int> dict  we cannot 'int' object is not iterable
# Int> set  we cannot 'int' object is not iterable


"""q=10
l=list(10)
print(l)
number=10
lisp=list(10)
print(lisp)
"""

print(":" * 60)

# int>boolean 1. if its positive value> True <class 'bool'> 2. if its negative its false
q = 23
b1 = bool(q)
print(b1, type(b1))
f = 0
b1 = bool(f)
print(b1, type(b1))
# possible> int> float, string , boolean

# Float
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# float>int
yes = 67.90
n1 = int(yes)
print(n1, type(n1))

# float to string

g = 90
s1 = str(g)
print(s1, type(s1))
print(g, type(g))

# float> list  we cannot 'float' object is not iterable
# float> tuple  we cannot 'float' object is not iterable
# float> dict  we cannot 'float' object is not iterable
# float> set  we cannot 'float' object is not iterable

q = 23.90
b1 = bool(q)
print(b1, type(b1))
f = 0
b1 = bool(f)
print(b1, type(b1))
# august 7th is not happen
# August 8th 2025

# string data conversion

# string > int
s1 = "new"
f1 = str(s1); print(s1, type(f1))
s1 = "87656"
f1 = str(s1)
print(s1, type(f1))
print(f1, type(s1))

# string to float its possible

s1 = "8.90"
f1 = float(s1)
print(f1, type(f1), f1 * 10)
# string to list is possible
str = "umadevi"
l = list(str)
print(l, type(l))

# string to dict

# string dosesnot follow the tersm dict as {}> so it doesnot suppoert
# string to set is possible it will normal store as random
s2 = "umadevi is cute girl"
set = set(s2)
print(set, type(set))

# string > boolean, if string is empty then conversion is false

"""s1={}
f1=bool(s1)
print(f1,type(f1))
#is false

s1={2,7,9,0}
f1=bool(s1)
print(f1,type(f1))
"""
# List

# List to int , float, string dict  (not importance) re not possible

"""l1 = [3, 5, 7, 8]
s1 = str(l1)
print(s1, type(s1), str[1])
#TypeError: 'str' object is not callable ---doubt

#list>tuple
"""
l2=[7,8,9,8]
#l9={7,9,5,4,3}
h=tuple(l2)

#Note:-#print(h,type(one single value converting to multiple is not possible


#dict >> int, float, string,list,tuple,set conversion is not posible

dict1={'a':145,'b':245}
l1=list(dict1)
print(l1 ,type(l1)) #only the (key) only convert dict

t1=tuple(dict1)
print(t1 ,type(t1)) #only the key only convert same in tuple also.

#set > int, float,string(not important),list,dict are not possible
set={4,6,8,9}
l1=list(set)
l1=tuple(set)
print(l1, type(l1)) #its converting random its not a list its a set and for tuple also








