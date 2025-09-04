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

list1 = [5, 3.5, 'Hello', [4, 6, 78], (3, 5, 7), {'a': 123}, {4, 7, 3}, True]
print(list1[2]) # Hello
print(list1[4]) # (3, 5, 7)
print(list1[3][2]) # 78
print(list1[-3]) # {'a': 123}
print(list1[-3]['a'])  # 123
print(list1[-4][2]) # 7

print("_"*50)
# Apply loop on list without index
list2 = [5, 7, 9, 10]
for val in list2:
    print(val, end=" ")
# 5 7 9 10

print()
# Apply loop on list with indexing
list_len = len(list2)
for i in range(list_len):
    print(i, list2[i])
"""
0 5
1 7
2 9
3 10
"""

print("_"*50)
##################### Slicing in the list ########
list3 = [5, 7, 3, 8, 23, 15, 'a', 'b', 16, 33, 45]
print(list3[0:6])  # [5, 7, 3, 8, 23, 15]
print(list3[0:12:2])  # [5, 3, 23, 'a', 16, 45]
print(list3[0::2])    # [5, 3, 23, 'a', 16, 45]
print(list3[-4:-9:-1]) # ['b', 'a', 15, 23, 8]
print(list3[-1:-12:-1]) # [45, 33, 16, 'b', 'a', 15, 23, 8, 3, 7, 5]
print(list3[::-1])  # [45, 33, 16, 'b', 'a', 15, 23, 8, 3, 7, 5]
print(list3[-1:-12:-2]) # [45, 16, 'a', 23, 3, 5]
print(list3[::-2]) # [45, 16, 'a', 23, 3, 5]

########################## List Methods #######################
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

print("_"*50)
################
# append method() : This method add data to the list as end of all values.
list_a = [4, 6, 8, 23, 5, 6]
list_a.append(20)
list_a.append("Hello")
print("list_a :",list_a)
# list_a : [4, 6, 8, 23, 5, 6, 20, 'Hello']


print("_"*50)
################
# insert(index, value) method() :  This method help us to add data at specific index position
list_b = [4, 6, 8, 23, 5, 6]
list_b.insert(2, 100)
print("list_b :", list_b)
# [4, 6, 100, 8, 23, 5, 6]

list_b.insert(7, 'Python')
print("list_b :", list_b)
# [4, 6, 100, 8, 23, 5, 6, 'Python']

print("_"*50)
################
# extend method :  we can insert one list data to another list
list_x = ['a', 'b', 'c']
list_y = [11, 22, 33]

list_y.extend(list_x)
print("list_y :", list_y)
# [11, 22, 33, 'a', 'b', 'c']

print("_"*50)
################
# list concatenation
list_p = [5, 7, 8]
list_q = ['x', 'y', 'z']

list_r = list_p + list_q
print("list_r :", list_r)
# [5, 7, 8, 'x', 'y', 'z']

#list_u = [5, 6, 7] + (2, 5, 7)
#print(list_u)
# can only concatenate list (not "tuple") to list

print("_"*50)
################
# list data reapitation
list_s = [5, 7, 23]
print(list_s*10)
# [5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23, 5, 7, 23]

print("Hello"*10)
# HelloHelloHelloHelloHelloHelloHelloHelloHelloHello


################
# removed method :  This method remove specific value  from list
# ->  if same value is available multiple times, then it will delete the first occurrence of the value
#

list_n = [5, 6, 7, 2, 5, 8, 5]
list_n.remove(5)
print("list_n :", list_n)
# [6, 7, 2, 5, 8, 5]

print("-"*50)
# ################
# pop(index) method : This method remove data from list using specific index position. the default index position
# is -1, pop method, return the removed data, that we can store in variable

list_r = [4, 6, 8, 22, 55, 88]
# removed data from default index -1
val = list_r.pop()
print("removed value :", val)
# removed value : 88
print("list_r :", list_r) # [4, 6, 8, 22, 55]


# remove value from specific index 2
val2 = list_r.pop(2)
print("removed value :", val2)
print("list_r:", list_r)  # [4, 6, 22, 55]
print(val2) # 8


print("_"*50)
###################################
# clear method :  This method remove all the data from list and remain empty list
list_rr = [4, 6, 8, 22, 55, 88, 242, 3]
list_rr.clear()
print("list_rr :", list_rr)
# list_rr : []



print("_"*50)
###################################
# del keyword to remove entire list value and variable from memory
list_yy = [4, 6, 8, 2]
del list_yy
#print("list_yy :", list_yy)
# NameError: name 'list_yy' is not defined

print("_"*50)
###############################
# del keyword to remove specific values from list using slicing
list_qq = [5, 7, 22, 15, 87, 12, 6]
del list_qq[2:5]  # This will remove these values # 22, 15, 87
print("list_qq :", list_qq)
# list_qq : [5, 7, 12, 6]


print("_"*50)
#############################
# replace the data from list using indexing or slicing
list_A = [5, 7, 22, 5, 17, 12, 34, 56]
list_A[2:5] = [100, 200, 300]   # These three values will replace 22, 5, 7
print("list_A :", list_A)
# [5, 7, 100, 200, 300, 12, 34, 56]
