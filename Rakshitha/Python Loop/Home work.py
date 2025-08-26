#write a code add all even number from 1 to 20
for i in range(2,20,2):
    print(i, end=" ")
# 2 4 6 8 10 12 14 16 18
#write a code to multiply value from 1 to 15
multiply=1
for i in range(1,15):
    print(multiply,"*",i,"=",multiply*i)
    multiply=multiply*i
"""
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
24 * 5 = 120
120 * 6 = 720
720 * 7 = 5040
5040 * 8 = 40320
40320 * 9 = 362880
362880 * 10 = 3628800
3628800 * 11 = 39916800
39916800 * 12 = 479001600
479001600 * 13 = 6227020800
6227020800 * 14 = 87178291200
"""
print("_"*50)
###################################################################

#1.write a python loops program of find those number which are divisible 7 and multiple of 5, between 1500  and 2700(both included
for i in range(1500,2700):
    if i%7==0 and i%5==0:
        print(i,end=" ")
# 1505 1540 1575 1610 1645 1680 1715 1750 1785 1820 1855 1890 1925 1960 1995 2030 2065 2100 2135 2170 2205 2240 2275 2310 2345 2380 2415 2450 2485 2520 2555 2590 2625 2660 2695

#2.python loops program to construct the folloeing pattern, using a neasted for loops
for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):
    print(i*"*")
"""
*
**
***
****
*****
****
***
**
*
"""
#3.python loops program that will add the word from the user to the empty string using python
"""
word=input("enter the word:")
str1=""
for i in range(len(word)):
    str1+=word[i]

print(str1)
"""
# enter the word:python
# python

#4.python loops program to count the number of even and odd number from a series of numbers using python.
numbers=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for val in numbers:
    if val%2==0:
        even+=1
    else:
        odd+=1
print("number of even numbers:",even)
print("number of odd numbers:",odd)
# number of even numbers: 4
# number of odd numbers: 5
#5.write a program that print all the number from 0 to 6 except 3 and 6 using python.
for i in range(1,10):
    if i !=3 or i !=6:
        print(i,end=" ")
# 1 2 3 4 5 6 7 8 9
print("_"*50)
#6.write a program that accepts a word from the user and converts all uppercses in the word to lowercases using python.
"""
input1=input("enter word:")
result=''
for char in input1:
    if char.isupper():
        print(char.lower(),end="")
    else:
        print(char,end=" ")
"""
# enter word:SQATOOLS
# sqatools
#7.python loop that accepts a string and calculate the number of digits and letters
word="python1234"
digit=0
character=0
for ele in word:
    if ele.isalpha():
        character +=1
    elif ele.isnumeric():
        digit+=1
print("digits:",digit)
print("character:",character)
# digits: 4
# character: 6
#8.to print the alphabet patter 'o' using python.
  # https://automationbysqatools.blogspot.com/2021/08/how-to-print-swastik-pattern-in-python.html
# HW: write a python program to design swastik pattern
""""
* * * - - - - - * * * * * * * * * * * *   i=1
* * * - - - - - * * * * * * * * * * * *   i=2
* * * - - - - - * * * - - - - - - - - -   i=3
* * * - - * - - * * * - - * - - - - - -   i=4
* * * - - - - - * * * - - - - - - - - -   i=5
* * * * * * * * * * * * * * * * * * * *   i=6
* * * * * * * * * * * * * * * * * * * *   i=7
- - - - - - - - * * * - - - - - - * * *   i=8
- - - - - * - - * * * - - * - - - * * *   i=9
- - - - - - - - * * * - - - - - - * * *   i=10
* * * * * * * * * * * - - - - - - * * *   i=11      
* * * * * * * * * * * - - - - - - * * *   i=12      
"""
for i in range(1,13):
    for j in range(1,21):
        if i == 1:
            if j in [1,2,3,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==2:
            if j in [1,2,3,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==3:
            if j in [1,2,3,6,9,10,11,16]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==4:
            if j in [1,2,3,9,10,11]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==5:
            if j in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==6:
            if j in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==7:
            if j in [9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==8:
            if j in [6,9,10,11,15,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==9:
            if j in [9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==10:
            if j in [1,2,3,4,5,6,7,8,9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==11:
            if j in [1,2,3,4,5,6,7,8,9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
"""
* * *           * * * * * * * * * * * * 
* * *           * * * * * * * * * * * * 
* * *     *     * * *         *         
* * *           * * *                   
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
                * * *             * * * 
          *     * * *       *     * * * 
                * * *             * * * 
* * * * * * * * * * *             * * * 
* * * * * * * * * * *             * * * 
"""























