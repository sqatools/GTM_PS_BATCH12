# write a python program to check the person is eligible to vote
age=18
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")
#eligible for vote
"""
age=int(input("Enter age:"))
if age>=18:
    print("You are eligible")
else:
    print("you are not eligible")
#Enter age:20
#You are eligible
"""
print("_"*50)
# write a python program to check number is divisible by 7 and 11.
n1=3
if n1%7==0 and n1%11==0:
    print("the number is divisible by 7 and 11:",n1)
else:
    print("the number is not divisible by 3 and 11:",n1)
#the number is not divisible by 3 and 11: 3

#1.  write a python program to show exam result as per marks received.
# marks greater than 30 and less than 50 :
"""
marks=int(input("enter your marks:"))
if marks >30 and marks <50:
    print("Pass with third division:")
else:
    print("not pass with third division:")
#enter your marks:40
#Pass with third division:
"""

#2. marks greater than 50 and less than 60:
"""
marks=int(input("enter your marks:"))
if marks >50 and marks <60:
    print("passed with first division:")
else:
    print("passed with second division:")
#enter your marks:50
#passed with second division:
"""
#3. marks greater than 50 and less than 60:
"""
marks=int(input("enter your marks:"))
if marks >60 and marks <80:
    print("passed with 1st division")
else:
    print("passed with 2nd division")
#enter your marks:70
#passed with 1st division
#enter your marks:60
#passed with 2nd division
"""
#marks greater than 80: passed with A excellent performance division
"""
marks=int(input("enter your marks:"))
if marks >80:
    print("passed with A excellent performance division")
else:
    print("not passed with A excellent performance division")
#enter your marks:100
#passed with A excellent performance division
#enter your marks:80
#not passed with A excellent performance division
"""
#marks less than 30: failed in exam
"""
marks=int(input("enter your marks:"))
if marks <30:
    print("passed in exam")
else:
    print("failed in exam")
#enter your marks:30
#failed in exam
"""
#python program to print the square of the number if it is divisible 11
"""
num=int(input("enter a number:"))
if num%11==0:
    print(num**2)
else:
    print("Number is not divisible by 11")
# enter a number:22
# 484
# enter a number:31
# Number is not divisible by 11
"""
#to check the authentication of username and password
"""
name=input("enter name:")
password=input("enter password:")
if name==password:
    print("it is valid")
else:
    print("it is not valid")
"""
# enter name:rakshitha
# enter password:1234
# it is not valid
print("_"*50)
#python program to validate user_id in the list of user_ids.
"""
id_list=[1,2,3,4,5,6,7,8]
id_=int(input("Enter ID number:"))
if id_ in id_list:
    print("valid ID")
else:
    print("Invalid ID")
"""
# Enter ID number:5
# valid ID
# Enter ID number:12
# Invalid ID

#