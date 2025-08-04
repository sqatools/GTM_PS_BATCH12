# try to solve this equation
# (a+b)^2=a^2+b^2+2ab
a = 5
b = 6
LHS = (a + b) ** 2
RHS = a ** 2 + b ** 2 + 2 * a * b
print(LHS == RHS)

# (a+b)3=a3+3ab(a+b)+b3
a = 3
b = 2
LHS = (a + b) * 3
RHS = a * 3 + 3 * a * b * (a + b) + b * 3
print(LHS == RHS)
result=a**3+3*a*b*(a+b)+b**3
print("(a+b)3:",result)
#(a+b)3: 125

# (a+b)+(a-b)=a^2-b^2
a = 3
b = 2
result = (a + b) * (a - b)
print("(a^2-b^2):", result)
# (a^2-b^2): 5
print("_" * 50)
# calculate the interst
# a=p(1+rt)
p = 1000
r = 10
t = 2
amount = p * (1 + r * t)
print("amountpayable:", amount)

# a=p(1+r/n)^nt
p = 1000
r = 10
n = 2
t = 2
amount = p * (1 + r / n) ** n * t
print("amount payable:", amount)

p = 1000
r = 10
t = 2
n = 2
amount = p + (p / r) * t
print("Amount payable: ", amount)

print("_" * 50)
# 1. Python program to add integer values.
num1 = 30
num2 = 40
print("Addition of num1+num2:", num1 + num2)
# Addition of num1+num2: 70

# 2.To subrtact twointeger values
num = 50
num = 25
print("subtraction of num1-num2:", num1 - num2)
# subtraction of num1-num2: -10

# 3.To multiplication of two numbers
num1 = 50
num2 = 100
print("multiplication of num1*num2:", num1 * num2)
# multiplication of num1*num2: 5000

# 4.to get average numbers
a = 10
b = 20
c = 30
print("Average of three:", (a + b + c) / 3)
# Average of three: 20.0

# 5.to print the square and cube of a given numbe.
n = 9
print("square of number:", n ** 2)
print("cube of number:", n ** 3)
# square of number: 81
# cube of number: 729

# 6.to interchange values btewwen varibles.
a = 10
b = 20
a,b=b,a
print("value of a:", a)
print("value of b:", b)
# value of a: 20
# value of b: 10

# 7.pythagorous therom
# (a2+b2=c2)
a=2
b=3
c=4
result=c*2
print("(a*2+b*2):",result)
# (a*2+b*2): 8
result=(a*2+b*2)
# (c*2): 10
print("(c*2):",result)
LHS=(a*2+b*2)
RHS=c*2
print(LHS==RHS)
# False

#8.calculate the simple intrest
# a=p+(p/r)t
p=1000
r=10
t=2
amount=p+(p/r)*t
print("amount payable:",amount)
# amount payable: 1200.0
print("_"*50)
# 9.calculate the area of circle
# radius=int(input("enter the radius of circle:"))
# area=13.14*radius*radius
# print("area of circle:",area)
#enter the radius of circle:4
# area of circle: 210.24

# 10.to print the current data in the given formate
import datetime
date = datetime.datetime.now()
print(date.strftime (" %y %b %d"))
#  25 Aug 04