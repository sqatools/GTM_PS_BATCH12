"""
if cond:
    code
else:
    code
"""

# compare 2 values with if condition
a1 = 40
b1 = 40

print(a1 == b1)

if a1 == b1:
    print("The values are equal:", a1, b1)
else:
    print("Values are not equal:", a1, b1)


print("_"*50)
############################################
# take input from user
# input function take value from user as string.
# user has to convert the data type as per his requirement
# val = input("Enter your value :")
# print(val, type(val))

"""
Enter your value :[65654, 764]
[65654, 764] <class 'str'>

"""

print("_"*50)
#####################################
"""
# check given number is odd or even
num1 = input("Enter your number:")
if int(num1)%2 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)
"""

"""
cond1  and cond2
True and True : True
False and True :  False
True and False :  False
False and False :  False 

cond1 or cond2
True or True : True
False or True :  True
True or False :  True
False or False :  False 

Operators:

> :  grater than
< :  less than
>= :  greater equal
<= :  less than equal
is : is operator
is not : is not operator
in : in operator
not in :  not in operator

"""

# write a python program to check given number is divisible by 3 and 5
n1 = 15

if n1%3 == 0 and n1%5 == 0:
    print("This number is divisible by 3 and 5 :", n1)
else:
    print("This number is not divisible by 3 and 5 :", n1)

print("_" * 50)

# write a python program to check given number is divisible by 3 or 5
n2 = 23

if n2%3 == 0 or n2%5 == 0:
    print("This number is divisible by 3 or 5 :", n2)
else:
    print("This number is not divisible by 3 or 5 :", n2)

# This number is not divisible by 3 or 5 : 23

############################################
# If - elif - else
"""
if cond1:
    code
elif code2:
    code
elif code3:
    code
else:
    code
"""

print("_"*50)
# write a python program to find the maximum value among three numbers.
a = 100
b = 70
c = 100
if a > b and a > c :
    print("A has greater value :", a)
elif b > a and b > c :
    print("B has greater value :", b)
elif c > a and c > b :
    print("C has greater value :", c)
else:
    print("No one has greater value")

# No one has greater value

# C has greater value : 60
# B has greater value : 70
# A has greater value : 100


# Home work
# Q1. write a python program to show exam result as per marks received.

marks = int(input("enter you marks :"))
# marks greater than 30 and less than 50 :  passed with 3rd division
# marks greater than 50 and less than 60 :  passed with 2nd division
# marks greater than 60 and less than 80 :  passed with 1st division
# marks greater than 80 :  passed with A Excellent Performance division
# marks less than 30 : Failed in exam
# marks greater than 100 : Invalid marks, can not be more than 100.

# Q2:  write a python program to check the person is eligible to vote
# take user age as input and if age is greater than 18 than, he can vote.

# Q3:  write a python program to check number is divisible by 7 and 11.

