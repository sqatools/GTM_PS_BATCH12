# Q1.  Write a python program to print square of the number if it is divisible by 3 or 7 else print cube
# Q2.  Calculate the electricity bill as per the unit consumed.
# get number of unit from user as input.
# if unit > 100 :  per unit charge is 15
# elif unit < 100 and unit > 200 :  per unit charge is 25
# elif unit > 200 :  per unit charge is 30
# else condition


#
# # Q1.  Write a python program to print square of the number if it is divisible by 3 or 7 else print cube
"""
num1 = 13
if num1%3 == 0 or num1%7 == 0:
    print("square value :", num1**2)
else:
    print("cube of the value :", num1**3)
"""
########################################################
# Q2.  Calculate the electricity bill as per the unit consumed.
# get number of unit from user as input.
# if unit < 100 :  per unit charge is 15
# elif unit > 100 and unit < 200 :  per unit charge is 25
# elif unit > 200 :  per unit charge is 30
# else condition

num_unit = int(input("Enter the number of units consumed :"))
if num_unit < 100:
    print("total bill as per 15/unit rate :", num_unit*15)
elif num_unit >= 100 and num_unit <= 200:
    print("total bill as per 25/unit rate :", num_unit*25)
elif num_unit > 200:
    print("total bill as per 30/unit rate :", num_unit * 30)
