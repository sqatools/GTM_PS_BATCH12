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
print("_"*50)
"""
*
* *
* * *
* * * *
* * * * *
"""


for i in range(1, 6):   # i =1, 2, 3
    for j in range(1, 6):  # range(1, 2), range(1, 3) ,  range(1, 4)
        print(j, end=" ")
    print()   # this print is resposible to change the line with \n



print("_"*50)
###################################

for i in range(1, 7): # i = 1
    for j in range(1, i+1):
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
for i in range(7, 1, -1): # i = 7 , 6
    for j in range(1, i):  # (1, 7) , (1, 6)
        print("_", end=" ")
    print()

print("_"*50)
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
for i in range(1, 8):   #  i = 1
    # INNER LOOP DECIDES NUMBER OF VALUES IN EACH LINE
    for j in range(1, 6):   #   j = (1, 6)
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











