#


for i in range(10, 16):
    for j in range(1, 6):
        print(j, end=" ")
    print(i)

"""
1 2 3 4 5 10
1 2 3 4 5 11
1 2 3 4 5 12
1 2 3 4 5 13
1 2 3 4 5 14
1 2 3 4 5 15
"""

print()
print("_" * 50)
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):  # i =1, 2, 3
    for j in range(1, 6):  # range(1, 2), range(1, 3) ,  range(1, 4)
        print(j, end=" ")
    print()  # this print is resposible to change the line with \n

print("_" * 50)
###################################

for i in range(1, 7):  # i = 1
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

"""
* 
* * 
* * * 
* * * * 
* * * * *     
* * * * * *     

"""

# reverse triangle pattern
for i in range(7, 1, -1):  # i = 7 , 6
    for j in range(1, i):  # (1, 7) , (1, 6)
        print("_", end=" ")
    print()

print("_" * 50)
# write a program to print a O pattern.
"""
  * * *    # i =1
*       *  # i =2 
*       *  # i =3
*       *  # i =4
*       *  # i =5
*       *  # i =6
  * * *    # i =7 
"""

# OUTER LOOP DECIDE TOTAL NUMBER OF LINES
for i in range(1, 8):  # i = 1
    # INNER LOOP DECIDES NUMBER OF VALUES IN EACH LINE
    for j in range(1, 6):  # j = (1, 6)
        if i in [1, 7]:
            if j in [1, 5]:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        elif i in [2, 3, 4, 5, 6]:
            if j in [1, 5]:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        else:
            print(j, end=" ")
    print()

"""
* 
* * 
* * * 
* * * * 
* * * * *     
* * * * * *     

"""
print("_" * 50)
# reverse triangle pattern
for i in range(7, 1, -1):  #
    print(i)
    for j in range(1, i):  # (1, 7) , (1, 6)
        print("_", end=" ")
    print()

print("_" * 50)

"""
* * * * * * # i = 1
* * * * * * # i = 2
    * *     # i = 3
    * *     # i = 4
    * *     # i = 5
    * *     # i = 6
"""

for i in range(1, 7):
    for j in range(1, 7):
        if i in [1, 2]:
            print("*", end=" ")
        elif i in [3, 4, 5, 6]:
            if j in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        else:
            print(" ", end=" ")

    print()

print("_" * 50)
"""
_ _ _ _ * _ _ _ _  i =1
_ _ _ * _ * _ _ _  i =2
_ _ * * * * * _ _  i =3
_ * _ _ _ _ _ * _  i =4
* _ _ _ _ _ _ _ *  i =5
"""
pt1 = "&"
pt2 = " "
for i in range(1, 6):
    for j in range(1, 10):
        if i == 1:
            if j == 5:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i == 2:
            if j in [4, 6]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")

        elif i == 3:
            if j in [3, 4, 5, 6, 7]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")

        elif i == 4:
            if j in [2, 8]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i == 5:
            if j in [1, 9]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        else:
            print("_", end=" ")

    print()  # This print statement help us to move to next line with default value \n

#HW: write a python program to design swastik pattern
# https://automationbysqatools.blogspot.com/2021/08/how-to-print-swastik-pattern-in-python.html
