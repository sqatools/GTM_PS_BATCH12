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

print("_" * 50)
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

print("_" * 50)
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

if n1 % 3 == 0 and n1 % 5 == 0:
    print("This number is divisible by 3 and 5 :", n1)
else:
    print("This number is not divisible by 3 and 5 :", n1)

print("_" * 50)

# write a python program to check given number is divisible by 3 or 5
n2 = 23

if n2 % 3 == 0 or n2 % 5 == 0:
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

print("_" * 50)
# write a python program to find the maximum value among three numbers.
a = 100
b = 70
c = 100
if a > b and a > c:
    print("A has greater value :", a)
elif b > a and b > c:
    print("B has greater value :", b)
elif c > a and c > b:
    print("C has greater value :", c)
else:
    print("No one has greater value")

# No one has greater value

# C has greater value : 60
# B has greater value : 70
# A has greater value : 100


# Home work
# Q1. write a python program to show exam result as per marks received.

# marks = int(input("enter you marks :"))
# marks greater than 30 and less than 50 :  passed with 3rd division
# marks greater than 50 and less than 60 :  passed with 2nd division
# marks greater than 60 and less than 80 :  passed with 1st division
# marks greater than 80 :  passed with A Excellent Performance division
# marks less than 30 : Failed in exam
# marks greater than 100 : Invalid marks, can not be more than 100.

# Q2:  write a python program to check the person is eligible to vote
# take user age as input and if age is greater than 18 than, he can vote.

# Q3:  write a python program to check number is divisible by 7 and 11.

####################################################
# Nested if condition
"""
if cond1:
    code
    if cond2:
        code
        if cond3:
            code
        else:
            code
    else:
        code
else:
    code

"""
print("_" * 50)
#  write a python to describe the interview process with the help of nested if condition

round1 = "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("congrats, 1st is cleared")
    if round2 == "pass":
        print("congrats, 2nd round is cleared")
        if round3 == "pass":
            print("congrats, 3rd round is cleared")
        else:
            print("Failed in last round")
    else:
        print("Failed in 2nd round")
else:
    print("Failed in 1st round")

print("_" * 50)
##############################
# single line of if condition checking
var = 21
output = "even" if var % 2 == 0 else "odd"
print("output :", output)

print("_" * 50)
###################################
# python code to check given value is available in the list
v1 = 12
v2 = 50
list1 = [3, 5, 7, 2, 45, 23, 12]
result = True if v1 in list1 else False
print("output2 :", result)
print(True if v1 in list1 else False)

if v1 in list1:
    print(f"v1: {v1} is available in list1: {list1}")
else:
    print(f"{v1} is not available in {list1}")

# check v2 is not available in the list1
if v2 not in list1:
    print(f"v2: {v2} is not available in list1: {list1}")
else:
    print(f"v2: {v2} is available in list1: {list1}")


print("-"*50)
########################################
# is, is not operator
# is operator compare 2 objects.
# == operator compare values of the object

list1 = [6, 8, 23, 45, 12]
list2 = [6, 8, 23, 45, 12]
list3 = list1


if list1 is list2:
    print("Both list objects are same")
else:
    print("Both list objects are not same")

print("_"*50)
if list1 == list2:
    print("Both list have same values")
else:
    print("Both list has diff values")



print("_"*50)

if list1 is list3:
    print("list1 and list3 objects are same")
else:
    print("list1 and list3 objects are not same")

# list1 and list3 objects are same


