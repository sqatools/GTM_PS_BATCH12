list1 = [5, 6, 'Hello', 3.2, [5, 6, 7]]

# get each value from list
for a in list1:
    print(a, type(a))

"""
5 <class 'int'>
6 <class 'int'>
Hello <class 'str'>
3.2 <class 'float'>
[5, 6, 7] <class 'list'>
"""
print("_" * 50)
######################### use range function in loop #############
"""
range(start, end, step) function.
->  range output include start and exclude the end value.
->  default start value is zero, if don't value any value.
->  default step value is 1, if dont provide the value
range(15)  # 15: end, default start value : 0, default step value : 1
range(2, 15) # 2: start, 15: end value, default step value : 1
range()

"""

print("_" * 50)
# range output include start and exclude the end value
for i in range(1, 10, 1):
    print(i)

"""
1
2
3
4
5
6
7
8
9

"""

print("_" * 50)
# print all odd value from 1 to 20
for j in range(1, 20, 2):
    print(j)

"""
1
3
5
7
9
11
13
15
17
19
"""

print("_" * 50)
# keep start value (0) and step value as default is 1
for k in range(15):
    print(k)

print("_" * 50)
# write a python program add all value from 1 to 10
# import pdb;
#
# pdb.set_trace()
add = 0
for val in range(1, 11, 1):
    add = add + val

print("sum of 1 to 10:", add)
# sum of 1 to 10: 55

print("_"*40)
############################################
# home work:
# 1. write a code add all even number from 1 to 20
# 2. write a code to multiply value from 1 to 15

for i in range(2, 20, 2):
    print(i, end="")

# 2 4 6 8 10 12 14 16 18

print("_"*40)
# 2. write a code to multiply value from 1 to 15
multiply = 1
for i in range(1, 15):
    print(multiply, "*", i, "=", multiply*i)
    multiply = multiply*i

print("_"*50)
##########################################
# Use if condition inside for loop

for i in range(1, 100):
    if i%7 == 0:
        print(i)

print("_"*40)
##################################
# program to tag each value as odd or even from 1 to 20
for j in range(1, 20):
    if j%2 ==0:
        print(j, ": even")
    else:
        print(j ,": odd")



print("_"*50)
##############################################
# write a program to check given number is prime or not
num = 7
prime = True
for i in range(2, num): # 2
    if num%i == 0: # 7%2 == 0 | 7%3 == 0 | 7%4 == 0 | 7%5 == 0 | 7%6 == 0
        prime = False

if prime:
    print("This is prime number :", num)
else:
    print("This is not prime number :", num)


print("_"*40)
########################################################
# Nested for loop :  In the nested loop for each single value of outer loop, entire inner loop will be executed.

for i in range(1, 5): # i = 1, 2, 3, 4
    print("Address : i:", i)
    for j in range(1, 3): # j =1, 2
        print("Package : j:", j)

    print("_"*50)


print("_"*50)
#########################################
# break and continue statement
# continue statement: if any condition met with continue statement, then it will not execute remaining code, it will move next interation of for loop.

for i in range(1, 10): # 1, 2
    if i in [2, 5, 7]:
        continue

    print(i)

"""
1
3
4
6
8
9
"""

print("_"*50)
# break statement: break statement will break the execution of the for loop if the condition is matching.

for i in range(1, 10):  # 1, 2
    if i == 5:
        break

    print(i)


print("_"*50)
################################################
# write a python code to get list of all the prime number between  1 to 100.

for num in range(1, 100): # num =1, 2, 3, 4
    prime = True
    for j in range(2, num): # (2, 4)
        if num%j == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
    else:
        continue

# 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

print()

print("_"*50)
##############################################
# write a python program to check two string are anagram to each other.
s1 = "aPython"
s2 = "yohtnP"
anagram = True

for char in s1:
    print(char)
    if char in s2:
        continue
    else:
        anagram = False
        break


if anagram == True and len(s1) == len(s2):
    print("These string are anagram :", s1, s2)
else:
    print("These string are not anagram :", s1, s2)


"""
num = 15
prime = True
for i in range(2, num): # 2
    print(i)
    if num%i == 0: # 7%2 == 0 | 7%3 == 0 | 7%4 == 0 | 7%5 == 0 | 7%6 == 0
        prime = False
        break
    else:
        continue
"""

