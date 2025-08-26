################ loop #######################
list1=[5,6,8,2,4]
#get each value from list
for var in list1:
    print(var)
"""
5
6
8
2
4
"""
list1=[5,6,8,2,4,'hello',3.2,[5,6,7]]
for a in list1:
    print(a,type(a))
"""
5 <class 'int'>
6 <class 'int'>
8 <class 'int'>
2 <class 'int'>
4 <class 'int'>
hello <class 'str'>
3.2 <class 'float'>
[5, 6, 7] <class 'list'>
"""
############## range function #################
#range() function
# range(start,end,step)
# range output inculde start and exculde the end value
for i in range(1,10,1):
    print(i)
"""
1
2
3
4
5
6
7
8
9
"""
print("_"*50)
#print all add value from 1 to 20
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
print("_"*50)
#keep start value (0) and step value as default is 1
for k in range(15):
    print(k)
"""
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
"""
#write a python program add all values from 1 t0 10
add=0
for val in range(1,11,1):
    add=add+val
print("sum of 1 to 10:",add)
# sum of 1 to 10: 55
#use if condition inside for loop
for i in range(1,100):
    if i%7==0:
        print(i)
"""
7
14
21
28
35
42
49
56
63
70
77
84
91
98
"""
print("_"*50)
#program to tag each value as odd or even from 1to20
for j in range(1,10):
    if j%2==0:
        print(j,":even")
    else:
        print(j,":odd")
"""
1 :odd
2 :even
3 :odd
4 :even
5 :odd
6 :even
7 :odd
8 :even
9 :odd
"""
#write a program to change given number is prime or not
num=23
prime=True
for i in range(2,num):
    if num%2==0:
        prime=False
if prime:
    print("this is prime number")
else:
    print("this is not prime number")
# this is prime number
################ Nested for loop ###################
for i in range(1,6):
    print("Address :i",i)
    for i in range(1,4):
        print("package:j",j)

    print("_"*50)
"""
Address :i 1
package:j 9
package:j 9
package:j 9
Address :i 2
package:j 9
package:j 9
package:j 9
Address :i 3
package:j 9
package:j 9
package:j 9
Address :i 4
package:j 9
package:j 9
package:j 9
Address :i 5
package:j 9
package:j 9
"""
for i in range(1,5):
    print("Address:i:",i)
    for j in range(1,3):
        print("Package:j:",j)

    print("_"*50)
"""
 Address:i: 1
Package:j: 1
Package:j: 2
__________________________________________________
Address:i: 2
Package:j: 1
Package:j: 2
__________________________________________________
Address:i: 3
Package:j: 1
Package:j: 2
__________________________________________________
Address:i: 4
Package:j: 1
Package:j: 2
"""
###### continue and break statement
# continue statement:
for i in range(1,10):
    if i in [2,5,7]:
        continue
    print(i,end=" ")
#1 3 4 6 8 9
print("_"*50)
for i in range(1,10):
    if i==5 :
        continue
    print(i,end=" ")
# 1 2 3 4 6 7 8 9
print("_"*50)
for i in range(1,10):
    if i==5 or i==7 or i==9:
        continue
    print(i,end=" ")
# 1 2 3 4 6 8
print("_"*50)

######### Break #####
#Break statement
for i in range(1,10):
    if i==5:
        break
    print(i,end=" ")
#1 2 3 4
print("_"*50)
#Write the python program to get list of all the number b/w 1 to 100
for num in range(1,100):
    prime=True
    for j in range(2,num):
        if num%j==0:
            prime=False
            break

    if prime:
        print(num,end=" ")
    else:
        continue
# 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
print("_"*50)
#Write a python program to check two string are anagram to each other
S1="python"
S2="yohtnp"
anagram=True
for char in S1:
    if char in S2:
        continue
    else:
        anagram=False
if anagram==True and len(S1)==len(S2):
    print("these string are anagram:",S1,S2)
else:
    print("there string are not anagram:",S1,S2)
#these string are anagram: python yohtnp
s1="python"
s2="yptnoha"
anagram=True
for char in s1:
    if char in s2:
        continue
    else:
        anagram=False
if anagram==True and len(s1)==len(s2):
    print("there string are anagram:",s1,s2)
else:
    print("there string are not anagram:",s1,s2)
#there string are not anagram: python yptnoha
s1 = "apython"
s2 = "yptnoh"
anagram = True
for char in s1:
    print(char)
    if char in s2:
        continue
    else:
        anagram = False
        break
# a
# if anagram == True and len(s1) == len(s2):
#     print("there string are anagram:", s1, s2)
# else:
#     print("there string are not anagram:", s1, s2)
print("_"*50)
s1 = "apython"
s2 = "yptnoh"
anagram = True
for char in s1:
    print(char)
    if char in s2:
        continue
    else:
        anagram = False
"""
a
p
y
t
h
o
n
"""

