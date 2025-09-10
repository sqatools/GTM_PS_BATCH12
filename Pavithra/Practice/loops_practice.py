#Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#Input1:1500
#nput2:2700

'''for i in range(1500, 2700):
    if i%7 == 0 and i%5 == 0:
        print(i)'''


print("-" *50)
#Python Loops program to construct the following pattern, using a nested for loops.
'''Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''

'''for i in range(1,6):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

for i in range(1,5):
    for j in range(i,5):
        print("*", end = " ")
    print()'''

#Python Loops program to count the number of even and odd numbers from a series of numbers using python.
#Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
'''tup1= (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for number in tup1:
    if number%2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Number of even numbers in this tuple: ", even)
print("Number of odd numbers in this tuple: ", odd)'''

#Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
'''for i in range(0,11):
    if i in (3,6):
        continue
    print(i, end= " ")'''

#write a program to print T pattern
'''print T pattern
* * * * * * # i = 1
* * * * * * # i = 2
    * *     # i = 3
    * *     # i = 4
    * *     # i = 5
    * *     # i = 6'''

'''for i in range(1,7):
    for j in range(1,7):
        if i in [1,2]:
            print("*", end=" ")
        elif i in [3,4,5,6]:
            if j in [3,4]:
                print("*", end= " ")
            else:
                print(" ", end=" ")
    print()'''

'''program to build below pyramid pattern
* * * * * * * * * 
  * * * * * * *   
    * * * * *     
      * * *       
        *         
 '''

for i in range(1,6):
    for j in range(1,10):
        if i in [1]:
            print("*", end=" ")
        elif i in [2]:
            if j in [2,3,4,5,6,7,8]:
                print("*", end= " ")
            else:
                print(" ", end=" ")
        elif i in [3]:
            if j in [3,4,5,6,7]:
                print("*", end= " ")
            else:
                print(" ", end= " ")
        elif i in [4]:
            if j in [4,5,6,]:
                print("*", end= " ")
            else:
                print(" ", end= " ")
        elif i in [5]:
            if j in [5]:
                print("*", end= " ")
            else:
                print(" ", end= " ")

    print()

print("_"*50)

#program for below pattern
'''     *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
'''
for i in range(1,6):
    for j in range(1,10):
        if i in [1]:
            if j in [5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [2]:
            if j in [4,5,6]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [3]:
            if j in [3,4,5,6,7]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [4]:
            if j in [2,3,4,5,6,7,8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [5]:
            if j in [1,2,3,4,5,6,7,8,9,10]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()


def function():
    for i in range(1,100):
        if i%11 == 0:
            print(i)

function()


