list2 = [1, 4, 7, 9]#Var name1
for a in list2: # here 'a' as var_name2 and list2 is var_name1
    print(a)
"""
#Syntax- for varname2 in var1name 'for var_name2 in var_name1'-For and in is imp keywords.
# we can take any variable name with any variable type
"""
"""
#Use Range function in Loop#
#Syntax-range (start value,end value,step) function
#Default start value is zero and default step value is 1
#range(15)-Means it will take by default start value as zero and end value is 15 and step value as default 1
#range(2,15)--Means it will take start value as 2 and end value is 14 and step value as default 1

print("*"*50)
for j in range(20):
    print(j)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
print("*"*50)
for j in range(20):
    print(j)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
for i in range (1, 10, 2): (1:start value;10 : end value;2:Step value)
  print(i)
#It will count from 1 as start value 10 as end value which will be less than end data means (1 to 9) and 2 means it define step here 
 # 1
# 3
# 5
# 7
# 9
"""
#Print all odd number from 1 to 20
print("*"*50)
for j in range(1,20,2):
    print(j)
"""
1
3
5
7
9
11
13
15
17
19
"""
# write a python program add all value from 1 to 10
"""
add=0
for a in range(1, 10, 1):
    add = a + add
print("Total:",add)

1
3
5
7
9
11
13
15
17
19
Total: 45

"""
# home work:
# 1. write a code add all even number from 1 to 20
# 2. write a code to multiply value from 1 to 15

# 1. write a code add all even number from 1 to 20
print("*"*50)
"""
for i in range (1,21,1):
    if(i%2 == 0):
     print("even number:",i)
    else:
        print("odd number:", i)
        
odd number: 1
even number: 2
odd number: 3
even number: 4
odd number: 5
even number: 6
odd number: 7
even number: 8
odd number: 9
even number: 10
odd number: 11
even number: 12
odd number: 13
even number: 14
odd number: 15
even number: 16
odd number: 17
even number: 18
odd number: 19
even number: 20

"""

#Another way of same programme
"""
for i in range(2, 20, 2):
    print(i,"", end="") 
    
#End ="" is a method to write the output in nsame line 
# "" is to create a space inbetween the value
"""
# 2. write a code to multiply value from 1 to 15
"""
multiply = 1
for i in range(1, 15):
    print(multiply, "*", i, "=", multiply*i)
    multiply = multiply*i

"""
################## For Loop using if condition##################

#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included).
"""
for var in range(1500,2701,1):
    if(var%7 == 0 and var%5 == 0):
        print(var,"",end="")
#Q=what would be the else condition here ?
"""
# write a program to check given number is prime or not

print("_"*40)
num = 7
prime = True
for i in range(2, num): # 2
    if num%i == 0:
        prime = False

if prime:
    print("This is prime number :", num)
else:
    print("This is not prime number :", num)
# Nested for loop :  In the nested loop for each single value of outer loop, entire inner loop will be executed.
print("_"*50)
""" 
for i in range(1, 5):
    print("Address : i:", i)
    for j in range(1, 3):
        print("Package : j:", j)
    for k in range (1,4) :
        print("Package : k:", k)
        
"""
"""
Address : i: 1
Package : j: 1
Package : j: 2
Package : k: 1
Package : k: 2
Package : k: 3
Address : i: 2
Package : j: 1
Package : j: 2
Package : k: 1
Package : k: 2
Package : k: 3
Address : i: 3
Package : j: 1
Package : j: 2
Package : k: 1
Package : k: 2
Package : k: 3
Address : i: 4
Package : j: 1
Package : j: 2
Package : k: 1
Package : k: 2
Package : k: 3
"""
#########################################
# break and continue statement
# continue statement: if any condition met with continue statement, then it will not execute remaining code, it will move next interation of for loop.
print("_"*40)
for i in range(1, 10):
    if i in [2, 5, 7]:
        continue
    print(i)
"""
3
4
6
8
9
"""
#Why print is written under if even the condition is mainly on For loop ?
#Break
print("_"*40)
for i in range(1, 10):
    if i in [2, 5, 7]:
        break
    print(i)
"""
1
"""

print("_"*40)
for i in range(7, 1, -1):  # i = 7 , 6
    for j in range(1, i):  # (1, 7) , (1, 6)
        print("j","",end="")
    print()
"""   
j j j j j j 
j j j j j 
j j j j 
j j j 
j j 
j
j
"""