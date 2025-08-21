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
if a == b:
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
########## Home Work-If else-Conditional Statement#######

#Prog-01-To print Highest Mark
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
## Q2:#Prog-02- write a python program to check the person is eligible to vote
# take user age as input and if age is greater than 18 than, he can vote.
"""
user1 = int(input("enter a number"))
if user1 >= 18:
      print("You are  eligible   to   vote")
else:
  print("You are NOT eligible to vote")

"""
### Q3:#Prog-03-write a python program to check number is divisible by 7 and 11.###
"""
print("_" * 50)
var1 = int(input("enter a number"))
if var1 % 7 == 0 and var1 % 11 == 0:
  print("Number is divisible by 7 and 11", var1) 
else:
  print("Number is divisible by 7 and 11", var1) 
#Number is divisible by 7 and 11 87
"""
#Q4:#Prog-04-If else program to get all the numbers divided by 3 from 1 to 30.
"""
a1 = int(input("enter a number"))
if a1 <= 30 :
    print("divided by 3", a1/3)
else :
    print("choose the number less than 30")
"""
#Q5:#Prog-05-to check whether the given number is divisible by 11 or not.
"""
num1 = int(input("enter a number"))
if num1%11 == 0 :
    print("Value of num1", (num1**2))
else :
    print("Number is not divisible by 11 choose some other number")
 """
# Single line of If condition checking
"""
num1 = int(input("enter a number"))
output=("Number is divisible by 11:",(num1**2)) if num1%11 == 0 else "Number is not divisible by 11 "
print("output:", output)

"""
#Prog-05-to check whether the given number is divisible by 14 or not.
"""
user2 =int(input("enter a number"))
if(user2%14==0):
    print("value of user2:",(user2*2))
else:
    print("Number is NOT divisible by 14")
    
# Output-value of user2: 56 
         3,Number is NOT divisible by 14 
"""
#Nested If-else Condition
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

""" 
 r1="fail"
r2="pass"
r3="pass"
if r1 == "fail":
    print("Congrats,your 1st round is cleared")
    if r2 == "pass":
       print("Congrats,your 2nd round is cleared")
       if r3 == "pass":
        print("Congrats,your 3rd round is cleared")
       else:
            print("Last round is NOT cleared")
    else:
       print("Sorry,your 2nd round is NOT cleared")
else:
   print("Failed in 1st round")
 
 """
#Have to ask why it is not working and why intenendation is a issue here
# what is the difference between elif and nested if condition
#Single line of if condition if more no of condition wont be there
"""
var=56
list1=[3,4,56,77,100]
output= True if var in list1 else False
print("Output is:",output)

if var in list1:
    print("var is available in list1",var)
else:
    print("var is NOT available  in list",var)
"""