
#Compare two values with if condition
"""a1 = 84
b1 = 84

if a1 == b1:
    print("Both values are equal")
else:
    print("Values are different")

print("_"*99)
#Take input from user
#input function take value from user as string
# User has to convert the data type as per his requirement

val = input("Enter your value:")
print(val, type(val))
print("_"*100)
#check given number is odd or even

num1 = input("Enter your number")
if int(num1)%2 == 0:
    print("This number is even number:", num1)
else:
    print("This number is odd number:", num1)

# Write a Python program to check given number is divisible by 3 and 5
n1 = 25
if n1%3 == 0 and n1%5 ==0:
    print("Number is divisible by 3 and 5:", n1)
else:
    print("This number is not divisible by 3 and 5")

"""
#If elif else
"""
if cond1:
    code
elif code2:
    code
else:
    code
"""
#Write a Python program to find highest value among 3 numbers
a = 84
b = 84
c = 84
if a>b and a>c:
    print("A has a greater value :", a)
elif b>a and b>c:
    print("B has a greater value :", b)
elif c>a and c>b:
    print("C has a greater value")
else:
    print("No number has greater value, all are equal")


# Write a Python program to show the result as per marks received
marks = int(input("Enter your marks:"))
if marks > 30 and marks<50:
    print("Passed with third division")
elif marks >50 and marks< 60:
    print("Passed with second class")
elif marks > 60 and marks <80:
    print("Passed with First class")
elif marks < 30:
    print("Failed in exam")
else:
    print("Passed with distinction")
