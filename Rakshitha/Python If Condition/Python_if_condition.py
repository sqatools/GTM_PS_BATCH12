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
