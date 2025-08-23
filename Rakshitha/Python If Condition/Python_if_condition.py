"""
If condition:
    code
else:
    code
"""
#Compare 2 values with if condition
a1=40
b1=70
print(a1==b1)
if (a1==b1):
    print("The values are equal:",a1,b1)
else:
    print("The values are not equal:",a1,b1)
#False
#The values are not equal: 40 70

a2=40
b2=40
print(a2==b2)
if (a2==b2):
    print("the values are equql",a2,b2)
else:
    print("the values are not equal:",a2,b2)
#True
#the values are equql 40 40
print("_"*50)
##########################
# take input from user
# input function take value from user as string
# user has to convert that data type as per requirement
# val=input("enter the value:")
# print(val, type(val))
#enter the value:551
#551 <class 'str'>
"""
# check the given number are odd or even
num1=input("Enter your number:")
if int(num1)%2==0:
    print("This is even number :", num1)
else:
    print("Then is odd number :", num1)
# Enter your number:55
# Then is odd number : 55
#Enter your number:40
#This is even number : 40
"""
#Write a program to check given number is divisble by 3 and 5
n1=25
if n1%3==0 and n1%5==0:
    print(" The number is divisible by 3 and 5:",n1)
else:
    print("The number is  not divisible by 3 and 5:",n1)
#The number is  not divisible by 3 and 5: 25

n1=15
if n1%3==0 and n1%5==0:
    print("the number is divisible by 3 and 5:",n1)
else:
    print("The number is not divisibe,3 and 5:",n1)
#the number is divisible by 3 and 5: 15
print("_"*50)

#Write a program to check given number is divisble by 3 or 5
n2=25
if n2%3==0 or n2%5==0:
    print("The number is divisible by 3 or 5:",n2)
else:
    print("The number is not divisible by 3 or 5:",n2)
#  The number is divisible by 3 or 5: 25

n1=18
if n1%3==0 or n1%5==0:
    print("The number is divisible by or 5:",n1)
else:
    print("The number is not divisible by 3 or 5:",n1)
# The number is divisible by 3 or 5: 18
print("_"*50)
## If - elif -else
"""
if cond1:
    code
elif2:
    code
else:
    code
"""
# write a python program to fine the maximum values among three numbers.
a=40
b=50
c=60
if a>b and a>c:
    print("A has greater value:", a)
elif b>a and b>c:
    print("B has greater value:", b)
elif c>a and c>b:
    print("C has greater value:", c)
else:
    print("No one has greater value")
#C has greater value: 60
a=40
b=70
c=60
if a>b and a>c:
    print("A has greater value:", a)
elif b>a and b>c:
    print("B has greater value:", b)
elif c>a and c>b:
    print("C has greater value:", c)
else:
    ("No one has greater value")
#B has greater value: 70

a=100
b=70
c=60
if a>b and a>c:
    print("A has greater value:", a)
elif b>a and b>c:
    print("B has greater value:", b)
elif c>a and c>b:
    print("C has greater value:", c)
else:
    print("No one has greater value")
# A has greater value: 100

a=100
b=50
c=100
if a>b and a>c:
    print("A has greater value:", a)
elif b>a and b>c:
    print("B has greater value:", b)
elif c>a and c>b:
    print("C has greater value:", c)
else:
    print("No one has greater value")
#No one has greater value
print("_"*50)
#Nested if condition:
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
#Write a python to describe the interview process with the help of neasted if condition

round1="fail"
round2="pass"
round3="pass"
if round1=="pass":
    print("congrats, 1st is cleared")
    if round2=="pass":
        print("congrats, 2nd round is cleared")
        if round3=="pass":
            print("congrats, 3rd round is cleared")
        else:
            print("congrats, 3rd round is cleared")
    else:
        print("failed in 2nd round")
else:
    print("failed in 1st round")
#failed in 1st round
print("_"*50)
round1="pass"
round2="fail"
round3="pass"
if round1=="pass":
    print("congrats, 1st round is cleared")
    if round2=="pass":
        print("congrats, 2nd round is cleared")
        if round3=="pass":
            print("congrats, 3rd round is cleared")
        else:
            print("failed in last round")
    else:
        print("failed, in 2nd round")
else:
    print("failed, in 1st round")
#congrats, 1st round is cleared
#failed, in 2nd round

print("_"*50)
round1 = "pass"
round2 = "pass"
round3 = "fail"
if round1 == "pass":
    print("congrats, 1st is cleared")
    if round2 == "pass":
        print("congrats, 1st round is cleared")
        if round3 == "pass":
            print("congrats, 3rd round is cleared")
        else:
            print("failed in last round")
    else:
        print("failed in 2nd round")
else:
    print("failed in 1st round")
#congrats, 1st is cleared
#congrats, 1st round is cleared
#failed in last round
print("_"*50)
#single line of if condition checking
var=20
output="even" if var%2==0 else "odd"
print("output:", output)
#output: even
var=21
output="even" if var%2==0 else "odd"
print("output:",output)
#output: odd
print("_"*50)

#### is operation/condition #####
# python code to check given values is available in the list
v1=13
v2=50
list1=[3,5,7,2,45,23,12]
output2=True if v1 in list1 else False
print("output:", output2)
#output: False

v1=12
output2=True if v1 in list1 else False
print("output:", output2)
print("True if v1 in list1 else False")
#output: True
#True if v1 in list1 else False
print("_"*50)

if v1 in list1:
    print("v1 is available in list1")
else:
    print("v1 is not available in list1,")
#v1 is available in list1
if 13 in list1:
    print("13 is available in list1")
else:
    print("13 is not available in list1:", list1)
#13 is not available in list1: [3, 5, 7, 2, 45, 23, 12]
print("_"*50)
if 13 in list1:
    print("v1 is available in list1")
else:
    print(f"{v1} is not available in {list1}")
#12 is not available in [3, 5, 7, 2, 45, 23, 12]

if v1 in list1:
    print(f" {v1} is available in {list1}")
else:
    print(f" {v1} is not available in {list1}")
# 12 is available in [3, 5, 7, 2, 45, 23, 12]
print("_"*50)
############ Not operation ############
# check v2 is not available in the list1
if v2 not in list1:
    print(f"v2:{v2} is not available in list1:{list1}")
else:
    print(f"{v2} is available in list1:{list1}")
print("_"*50)
######## is , not operation ############
list1=[6,8,23,45,12]
list2=[6,8,23,45,12]
list3=list1
if list1 in list2:
    print("both list object are same")
else:
    print("both list object are not same")
#both list object are not same

if list1==list2:
    print("both list have same values")
else:
    print("both list has different values")
#both list have same values

if list1 is list3:
    print("list1 and list3 objects are same")
else:
    print("list1 and list3 objects are not same")
# list1 and list3 objects are same
