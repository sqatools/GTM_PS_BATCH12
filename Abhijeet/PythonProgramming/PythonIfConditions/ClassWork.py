# Q1.  Write a python program to print square of the number if it is divisible by 3 or 7 else print cube
# Q2.  Calculate the electricity bill as per the unit consumed.
# get number of unit from user as input.
# if unit > 100 :  per unit charge is 15
# elif unit < 100 and unit > 200 :  per unit charge is 25
# elif unit > 200 :  per unit charge is 30
# else condition

#Write a python program to print square of the number if it is divisible by 3 or 7 else print cube
num1 = 13
if num1%3 ==0 or num1%7 == 0:
    print("square value:", num1**3)
else:
    print("cube of the value:", num1**3)

""" Calculate the electricity bill as per the unit consumed
Get number of unit from user as input
if unit < 100: per unit charge is 15
elif unit > 100 and unit < 200 unit charge is 25
"""

num_unit = int(input("Enter the number of units consumed"))
if num_unit<= 100:
    print("Price per unit is 15")
    print("Total bill as per 15rs/unit rate:", num_unit*15)
elif num_unit >100 and num_unit <= 200:
    print("Total bill is as per 25 rs/ unit rate:", num_unit*25)
elif num_unit > 200:
    print("Total bill as per 30/unit rate:", num_unit *30)
