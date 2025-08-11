#Syntax of If-Else#
"""
if cond:
  code
else:
  code
  """
#PG-01#Compare if True or False between two variables
a = 30
b = 70
if a ==b:
 print("value of A:",'a is true')
else:
  print("value of A:",'a is false')
print("_" * 50)
  #print("value of A:"a is true)

#PG-01#Compare if True or False between two variables-Another way
print("_"*50)
a = 40
b = 90
if a==b:
    print("A value is equal to B",a,b)
else:
    print("A value is not equal to B",a,b)
    #A value is not equal to B 40 90
print("_"*50)
#PG-02-Python program to check given number is divided by 3 or not.
a = 24
if a%3==0 :
    print("Value of A is even:",a) #Value of A is even: 24
else:
    print("Value of A is odd:",a)
print("_" * 50)
    #

# PG-03-Python program to check given number is Odd and Even number
"""
print("_"*50)
a = int(input("Enter your number"))
if a%2==0:
    print("Number is even:",a)
else:
    print("Number is odd:",a) #Number is odd: 23
"""


#########-Python program to check given number is Odd and Even number by using input method#
"""
print("_" * 50)
num1 = input("Enter your number:")
if int(num1)%2 == 0:
    print("This is even number :", num1) #This is even number : 12
else:
    print("This is odd number :", num1) #Number is odd: 33
print("_" * 50)
"""

#PG-04-Python program to check given number is divided by 2 and 7#
"""
var = 23
if var%2 == 0 and var%7 == 0:
    print("Number is divided by 3 and 7", var)
else:
    print("Number is NOT divided by 3 and 7", var)

#############
var = 27
if var%2 == 0 and var%7 == 0:
    print("Number is divided by 3 and 7", var)
else:
    print("Number is NOT divided by 3 and 7", var) #Number is NOT divided by 3 and 7 27
    
    """
########## Home Work-To print Highest Mark#######

"""
print("_" * 50)
Mark = int(input("enter a number"))
if (Mark <= 30):
  print("Failed",Mark)
elif(Mark >= 30 and Mark <=50):
 print ("Passed with 3rd division",Mark)
elif (Mark >= 50 and Mark <= 80):
     print("Passed with 2nd division", Mark)
elif (Mark >= 80 and Mark <= 100):
    print("Passed with an excellent division ",Mark)
else:
  print("Invalid marks",Mark)

"""

"""
## Q2:  write a python program to check the person is eligible to vote
# take user age as input and if age is greater than 18 than, he can vote.

user1 = int(input("enter a number"))
if user1 >= 18:
      print("You are  eligible   to   vote")
else:
  print("You are NOT eligible to vote")

"""
### Q3:  write a python program to check number is divisible by 7 and 11.###
"""
print("_" * 50)
var1 = int(input("enter a number"))
if var1 % 7 == 0 and var1 % 11 == 0:
  print("Number is divisible by 7 and 11", var1)
else:
  print("Number is divisible by 7 and 11", var1)

"""
