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


print("_"*50)
######################################
# count method :  This method return the count/occurrences of any specific value in the list
list_11 = [4, 6, 8, 4, 6, 8, 3, 4]
print("count of 6 :", list_11.count(6))  # count of 6 : 2
print("count of 4 :", list_11.count(4))  # count of 4 : 3


print("_"*50)
######################################
# index method :  This method return index position of any value in list
list_11 = [4, 6, 18, 4, 16, 8, 13, 4]
print("index of 16 :", list_11.index(16))
# index of 16 : 4


print("_"*50)
######################################
# sort method : Sort method can sort the list values in ascending or descending order. It updates the original
# list values
list_11 = [4, 6, 18, 4, 16, 8, 13, 14]
# sort list values in ascending order
list_11.sort()
print("list_11:", list_11)  # [4, 4, 6, 8, 13, 14, 16, 18]

list_12 = [17, 6, 18, 4, 16, 8, 13, 14]
# sort in descending order
list_12.sort(reverse=True)
print("list_12 :", list_12)
# [18, 17, 16, 14, 13, 8, 6, 4]

print("_"*50)
######################################
# sorted function : this function sort the list values in both ascending or descending order.
# sorted function does not modify the original list values.
list_13 = [11, 6, 18, 5, 16, 8, 10, 14]
result1 = sorted(list_13)
result2 = sorted(list_13, reverse=True)
print("ascending result :", result1) # [5, 6, 8, 10, 11, 14, 16, 18]
print("descending result :", result2) # [18, 16, 14, 11, 10, 8, 6, 5]


print("_"*50)
######################################
# reverse method : This method reverse the list values and modify original list
list_14 = [5, 6, 7, 22, 55, 11]
list_14.reverse()
print("list_14 :", list_14)
# list_14 : [11, 55, 22, 7, 6, 5]


print("_"*50)
######################################
# reversed function : This function reverse the list values and does not modify the original list
list_15 = [5, 6, 7, 22, 55, 11, 15, 37]

result = list(reversed(list_15))
print("reverse values :", result)
# [37, 15, 11, 55, 22, 7, 6, 5]



print("_"*50)
######################################
# copy content from one list to another list

# Shallow copy :  When we assign one list data to another list, then it is called shallow copy
# -> In this concept, if we will modify any list data, then changes will reflect on the both lists.

list_P = [5, 7, 9, 2, 15]
list_Q = list_P
list_Q.append(100)
list_P.append(200)

print("list_p :", list_P) # [5, 7, 9, 2, 15, 100, 200]
print("list_Q :", list_Q) # [5, 7, 9, 2, 15, 100, 200]

###############################################
# Deep copy : In deep copy if we will do changes in one list, then it will not reflect in another list.

list_x = [5, 7, 33, 55, 66, 7]
list_y = list_x.copy()

list_y.append(500)
list_x.append(600)
list_x.append(800)
list_y.append('Python')
print("list_x :", list_x) # [5, 7, 33, 55, 66, 7, 600, 800]
print("list_y :", list_y) # [5, 7, 33, 55, 66, 7, 500, 'Python']


print("_"*50)
#####################################################
############## Max, min, sum #######################

list_15 = [5, 7, 33, 55, 66, 7, 600, 800]
print("Max value :", max(list_15)) # Max value : 800
print("Min value:", min(list_15)) # Min value: 5
print("Sum of values :", sum(list_15)) # Sum of values : 1573

print("_"*50)
######################### List comprehension ###############
list1 = [4, 8, 7, 2, 6, 9, 12, 13]

# write a program to get odd values
for val in list1:
    if val%2 != 0:
        print(val, end=" ")
    else:
        continue

# 7 9 13

# solve program with list comprehension
result = [val for val in list1 if val%2 != 0]
print("result :", result)
# result : [7, 9, 13]


########### nested loop with list comprehension ############
list_2 = ['a', 'b', 'c']
list_3 = ['p', 'q']
#output = [('a', 'p'), ('a', 'q'), ('b', 'p'), ('b', 'q'), ('c', 'p'), ('c', 'q')]

result2 = [(x, y) for x in list_2 for y in list_3]
print("result 2:", result2)
# [('a', 'p'), ('a', 'q'), ('b', 'p'), ('b', 'q'), ('c', 'p'), ('c', 'q')]