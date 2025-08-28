"""
while condition:
    code
"""

n= 1
while n < 10:
    print(n)
    n = n + 1
    # n += 1


# infinite loop
n= 1
while True:
    print(n)
    n = n + 1
    if n == 1000:
        break



##############################
# write a program to reverse a number with the help of while loop
#num = 123   # output = 321
num = 9876543
rev = 0

while num > 0: # 123 > 0 | 12 > 0 | 1> 0 | 0 > 0
    temp = num%10 # 3, 2, 1
    rev = rev*10 + temp # 0*10 + 3 = 3 | 3*10 + 2 = 32 | 32*10 + 1 = 321
    num = num//10  # 12, 1, 0

print("reverse output :", rev)

print("_"*50)
#########################################
# write a program to get fibonacci series
# 0 1 1 2 3 5 8 13 21 33
a = 0
b = 1
# print(a, end=" ")
# print(b, end=" ")
for _ in range(20): #a  b | a  b | a  b| a  b |a, b |
    a, b = b, a+b #  1, 1 | 1, 2 | 2, 3| 3, 5 |5, 8 |
    print(b, end=" ") # 1, 2, 3, 5, 8

# 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946

########################################
# write a python get summation all the list values
list1 = [5, 7, 9, 12, 45, 67]

