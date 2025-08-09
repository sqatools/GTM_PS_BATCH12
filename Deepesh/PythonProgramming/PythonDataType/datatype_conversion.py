##################### Integer ##################
#### int ->  float ######
n1 = 50
f1 = float(n1)
print(f1, type(f1))  # 50.0 <class 'float'>


print("_"*50)
#### int ->  string ######
n2 = 785
s2 = str(n2)
print(s2, type(s2)) # 785 <class 'str'>
print(s2[1]) # 8

print("_"*50)
#### int ->  list ###### # conversion is not possible
"""
n3 = 987987
l3 = list(n3)
print(l3)
# TypeError: 'int' object is not iterable
"""

#### int ->  tuple ###### # conversion is not possible
#### int ->  dict ###### # conversion is not possible
#### int ->  set ###### # conversion is not possible

print("_"*50)
#### int ->  boolean ######

a1 = 0
b1 = bool(a1)
print(b1, type(b1)) # False <class 'bool'>

a2 = 567576
b2 = bool(a2)
print(b2, type(b2)) # True <class 'bool'>

##################################### Float  ################################
print("_"*50)
#### float ->  int ######
f1 = 67.77
n1 = int(f1)
print(n1, type(n1))  # 67 <class 'int'>


print("_"*50)
#### float ->  string ######
f2 = 87.45
s2 = str(f2)
print(s2, type(s2), s2[3])
# 87.45 <class 'str'> 4

print("_"*50)
#### float ->  list ###### conversion is not possible
#### float ->  tuple ###### conversion is not possible
#### float ->  dict ###### conversion is not possible
#### float ->  set ###### conversion is not possible


print("_"*50)
#### float ->  boolean ######
f1 = 0.0
b1 = bool(f1)
print(b1, type(b1)) # False <class 'bool'>

f2 = 89.78
b2 = bool(f2)
print(b2, type(b2)) # True <class 'bool'>

print("_"*50)
##################################### string  ################################
# string -> int ##
# notes :  if string contains any word/char then conversion is not possible
# if string contains only number then conversion is  possible

s1 = "7897"
print(s1, type(s1), s1[0])
n1 = int(s1)
print(n1, type(n1))  # 7897 <class 'int'>
print(n1*2) # 15794


print("_"*50)
### string -> float ###
s2 = "8.97"
f2 = float(s2)
print(f2, type(f2), f2*10)
# 8.97 <class 'float'> 89.7


print("_"*50)
### string -> list/tuple ####
str3 = "Python"
l3 = list(str3)
t3 = tuple(str3)
print(l3, type(l3))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

print(t3, type(t3))
# ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>


print("_"*50)
### string -> dict #### conversion is not possible
### string -> set ####
s5 = "Programming"
set3 = set(s5)
print(set3, type(set3))
# {'i', 'P', 'r', 'n', 'g', 'm', 'a', 'o'} <class 'set'>



# string -> boolean # behave like int
# if string is empty then conversion is False
# if string contains some value, then conversion is True


###################################### List ############################
# list -> int # conversion is not possible
# list -> float # conversion is not possible
# list -> string # not important
l1 = [3, 5, 7, 8]
str1 = str(l1)
print(str1, type(str1), str1[0], str1[1])
# [3, 5, 7, 8] <class 'str'> [ 3

print("_"*50)
# list -> tuple
l2 = [5, 7, 3, 45]
t2 = tuple(l2)
print(t2, type(t2))
# (5, 7, 3, 45) <class 'tuple'>

print("_"*50)
### list -> dict ### conversion is not possible
### list ->  set ###
l3 = [5, 7, 3, 6, 7, 5, 3]
s3 = set(l3)
print(s3, type(s3))
# {3, 5, 6, 7} <class 'set'>

# list -> boolean ## same as int, string

###################### Tuple ########################
# Tuple -> int ### conversion is not possible
"""
t2 = (4, 5)
n1 = int(t2)
print(n1)
"""
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'

# Tuple -> float ### conversion is not possible
# Tuple -> string ### not important
# Tuple -> list ###
t1 = (5, 7, 2, 78, 34)
l1 = list(t1)
print(l1, type(l1))
# [5, 7, 2, 78, 34] <class 'list'>

##### Tuple -> dict ### conversion is not possible
##### tuple -> set ###
t3 = (5, 7, 2, 78, 34, 6, 7, 2)
s3 = set(t3)
print(s3, type(s3))
# {2, 34, 5, 6, 7, 78} <class 'set'>

#################### Dict ################
# dict -> int ### conversion is not possible
# dict -> float ### conversion is not possible
# dict -> string ### not important
# dict -> list/tuple/set ### conversion is not possible
dict1 = {'a': 123, 'b' : 3456, 'c': 567}
l1 = list(dict1)
print(l1, type(l1))  # ['a', 'b', 'c'] <class 'list'>

t1 = tuple(dict1)
print(t1, type(t1))  # ('a', 'b', 'c') <class 'tuple'>

s1 = set(dict1)
print(s1, type(s1))  # {'b', 'c', 'a'} # <class 'set'>

print("_"*50)
#################### set ################
# set -> int ### conversion is not possible
# set -> float ### conversion is not possible
# set -> string ### not important
# set -> list ### conversion is not possible
s1 = {5, 7, 23, 56, 7, 12}
l1 = list(s1)
print(l1, type(l1))
# [23, 5, 7, 56, 12] <class 'list'>

t1 = tuple(s1)
print(t1, type(t1))
# (23, 5, 7, 56, 12) <class 'tuple'>

# set -> dict ### conversion is not possible