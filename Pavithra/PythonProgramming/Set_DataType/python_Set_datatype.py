"""
# Properties:
->  Set is mutable data type, we can modify the data at point of time.
->  Set contains data in curly braces, {}
->  Set store values in random order.
->  Set only store unique values, it means duplicate values are not allowed.
    if try to add same values multiple times, it will consider the one time only.
->  Set only contains immutable data type as set member. e.g int, float, complex, string, tuple, boolean.
"""

set1 = {3, 'Hello', 3.5, True, (3, 50, 6), 3}
print(set1, type(set1), id(set1))
# {True, 3, 3.5, 'Hello', (3, 50, 6)}
# {True, 3, 3.5, 'Hello', (3, 50, 6)} <class 'set'> 2901399962784


# set2 = {3, 'Hello', 3.5, True, (3, 50, 6), 3, [4, 7, 9]}
# print(set2, type(set2))
# TypeError: unhashable type: 'list'

########################### Set methods #################
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

"""
print("_" * 50)
##### add data to the set ####
set_4 = {4, 6, 'a', 8, 2}
set_4.add('Python')

print("set4 :", set_4)
# {2, 4, 6, 8, 'Python'}


print("_" * 50)
##############################
# update method: This method help us to update one set data to another set.
set_5 = {4, 6, 'a', 8, 2}
set_6 = {'x', 'y', 'z'}
set_6.update(set_5)

print("set_5 :", set_5)  # {'a', 2, 4, 6, 8}
print("set_6 :", set_6)  # {2, 4, 6, 8, 'x', 'a', 'z', 'y'}

print("_" * 50)
##############################
# union method: This method combine 2 sets values and create a new set.
set_5 = {4, 6, 'a', 8, 2}
set_6 = {'x', 'y', 'z'}

result = set_5.union(set_6)
print("union result :", result)
# union result : {2, 4, 'a', 6, 'x', 8, 'y', 'z'}


print("_" * 50)
##############################
# difference method: different method return the difference of values from one set to another set
set_7 = {4, 6, 'a', 8, 2, 'x', 'y'}
set_8 = {'x', 'y', 'z', 2, 8}

diff_7_8 = set_7.difference(set_8)
print("different from set7 to set8 :", diff_7_8)  # {4, 6, 'a'}

diff_8_7 = set_8.difference(set_7)
print("different from set8 to set7 :", diff_8_7)  # {'z'}
# different from set8 to set7 : {'z'}

##### difference update  method ####
# difference update method get the difference between 2 sets and update the result in specific set.
set_7.difference_update(set_8)
print("set_7 :", set_7)  # {4, 6, 'a'}
print("set_8 :", set_8)  # {'z', 2, 'x', 'y', 8}

print("_" * 50)
##############################
# intersect method: Intersection method return common values between 2 sets
set_9 = {4, 6, 'a', 8, 2, 'x', 'y'}
set_10 = {'x', 'y', 'z', 2, 8, 11}

intersect_output = set_10.intersection(set_9)
print("intersect_output :", intersect_output)
# {8, 2, 'y', 'x'}

print("set_9 :", set_9)
print("set_10 :", set_10)

print("_" * 50)
####################################
# intersection update :  intersection update method find the common values between 2 sets and update
#                        result in any of the existing set.
set_9.intersection_update(set_10)
print("set_9 :", set_9)  # {8, 'x', 2, 'y'}
print("set_10 :", set_10)  # {'x', 2, 8, 'y', 11, 'z'}

print("_" * 50)
####################################
# symmetric different method: This method return the difference values from both the sets.

set_A = {1, 2, 3, 'A', 'B', 'C'}
set_B = {1, 2, 3, 'P', 'Q', 'R'}

result = set_A.symmetric_difference(set_B)
print("symmetric_difference result :", result)
# {'P', 'B', 'A', 'R', 'C', 'Q'}

print("set_A :", set_A)  # {1, 2, 3, 'B', 'A', 'C'}
print("set_B :", set_B)  # {1, 2, 3, 'Q', 'R', 'P'}

print("_" * 50)
####################################
# symmetric different update method : This method get difference between both sets and update result in
# any existing set.

set_A.symmetric_difference_update(set_B)
print("set_A :", set_A)  # {'Q', 'A', 'C', 'B', 'R', 'P'}
print("set_B :", set_B)  # {1, 2, 3, 'Q', 'R', 'P'}

print("_" * 50)
####################################
# remove method : This method remove any specific value from given set, if value is not available then
# it will throw KeyError
set_j = {'Q', 'A', 'C', 'B', 'R', 'P', 'D'}
# remove existing value
set_j.remove('A')
print("set_j :", set_j)  # {'R', 'P', 'B', 'D', 'C', 'Q'}

# remove non-existing value
# set_j.remove("W")
# print("set_j :", set_j)
# KeyError: 'W'

print("_" * 50)
####################################
# discard method : This method remove any specific value from given set
# if the value is not available in the set, then it will not throw any error.
set_k = {33, 66, 23, 77, 88}

# remove existing value
set_k.discard(23)
print("set_k :", set_k)  # {33, 66, 88, 77}

# remove non-existing value
set_k.discard(100)
print("set_k :", set_k)

print("_" * 50)
####################################
# pop method :  This method remove any value from set and return it

set_l = {33, 66, 23, 77, 88, 200}
val = set_l.pop()
print("removed value  :", val)  # 33
print("set_l values :", set_l)  # {66, 23, 200, 88, 77}


print("_" * 50)
####################################
# issuperset and issubset method :
# ->  superset method return True if set_A has all value of set_B along with other value, then set_A is supper set
# ->  subset method return True if set_B is child of set_A data set.

set_x = {2, 3, 5, 'a', 'b', 'c'}
set_y = {2, 3, 'b'}
set_z = {5, 'a', 'd'}
print("check is superset for set_x and set_y:", set_x.issuperset(set_y))
# check is superset for set_x and set_y: True

print("check is superset for set_x and set_z:", set_x.issuperset(set_z))
# check is superset for set_x and set_z: False


print("check is subset for set_y and set_x:", set_y.issubset(set_x))
# check is subset for set_y and set_x: True


print("_"*50)
################# apply loop on set ############

set_n = {5, 7, 9, 12, 13, 'a', 'b'}
for val in set_n:
    print(val)

"""
b
5
7
9
a
12
13
"""



###############################################
# write a python program to get values which are divisible by 2, 3 and 5 from 1 to 100


# write a python to get all Capital letter from given string.
str1 = "We aRe LeArNing PytHon PrograMming"
output = "WRLANPHPM"



