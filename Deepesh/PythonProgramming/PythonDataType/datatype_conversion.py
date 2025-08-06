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