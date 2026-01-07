"""
# Properties:
->  Set is mutable data type, we can modify the data at point of time.
->  Set contains data in curly braces, {}
->  Set store values in random order.
->  Set only store unique values, it means duplicate values are not allowed.
    if try to add same values multiple times, it will consider the one time only.
->  Set only contains immutable data type as set member. e.g int, float, complex, string, tuple, boolean.
"""
set1={3,'hello',3.5,True,(3,50,6),3 }
print(set1) #{True, 'hello', 3, 3.5, (3, 50, 6)}

set1={3,'hello',3.5,True,(3,50,6),3 }
print(set1,type(set1),id(set1))
# {True, 3, 3.5, 'hello', (3, 50, 6)} <class 'set'> 2741384632960

# set2={3,'hello',3.5,True,(3,50,6),3,[4,7,9]}
# print(set2,type(set2))
# TypeError: unhashable type: 'list'

################## Set methods ###################
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

#### Add data type set ##########
set_4 ={4,6,8,2}
set_4.add('python')
print("set_4:",set_4)  #set_4: {2, 4, 6, 8, 'python'}


print("_"*50)
# update method :- This method help us to update one set data to other set
set_5 = {4,6,'a',8,2}
set_6 = {'x','y','z'}
set_6.update(set_5)
print("set_5:",set_5)    #set_5: {2, 4, 6, 'a', 8}
print("set_6:",set_6)    #set_6: {2, 4, 6, 8, 'x', 'y', 'z', 'a'}

print("_"*50)
# union method :- this method combin 2 set values and creat a new set
set_5 = {4,6,'a',8,2}
set_6 = {'x','y','z'}
result =set_5.union(set_6)
print("union result:",result)
# union result: {2, 'z', 4, 'y', 6, 8, 'a', 'x'}

# difference method :- this method combin 2 sets values and creat a new set
set_7 = {4,6,'a',8,2,'x','y'}
set_8 ={'x','y','z',2,8}
diff_7_8 =set_7.difference(set_8)
print("different from set7 to set8:",diff_7_8)
# different from set7 to set8: {4, 6, 'a'}

print("_"*50)
############# difference update method############
# difference update method get the difference between 2 sets and update the result in specific set.
set_7.difference_update(set_8)
print("set_7:",set_7)
print("set_8:",set_8)
set_7: {4, 6, 'a'}
set_8: {'y', 2, 'z', 8, 'x'}

diff_8_7 = set_8.difference(set_7)
print("different from set8 to set7:",diff_8_7)
# different from set8 to set7: {'z'}

print("_" * 50)
##############################
# intersect method: Intersection method return common values between 2 sets
set_9 = {4, 6, 'a', 8, 2, 'x', 'y'}
set_10 = {'x', 'y', 'z', 2, 8, 11}
intersect_output =set_10.intersection(set_9)
print("intersect_output:",intersect_output)
# intersect_output: {8, 2, 'x', 'y'}

print("set_9 :", set_9)
print("set_10 :", set_10)
# set_9 : {'x', 2, 4, 'y', 6, 8, 'a'}
# set_10 : {'x', 2, 'y', 'z', 8, 11}

print("_"*50)
####################################
# intersection update :  intersection update method find the common values between 2 sets and update
#                        result in any of the existing set.
set_9.intersection(set_10)
print("set_9:",set_9)   #set_9: {'y', 2, 4, 6, 'x', 8, 'a'}
print("set_10:",set_10)  #set_10: {'y', 2, 'z', 'x', 8, 11}

print("_" * 50)
####################################
# symmetric different method: This method return the difference values from both the sets.












