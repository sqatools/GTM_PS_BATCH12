#
for i in range(10,16):
    for j in range(1,6):
        print(j,end=" ")
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
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
"""
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end=" ")
    print()# this print is resposible to change the line with \n
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *
"""
print("_"*50)
for i in range(1,8):
    for j in range(2,5):
        print("$",end=" ")
    print()
"""
 $ $ $ 
$ $ $ 
$ $ $ 
$ $ $ 
$ $ $ 
$ $ $ 
$ $ $ 
"""
print("_"*50)
# Reverse triangle pattern
for i in range(7,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
"""
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
# write a python program to print 0 pattern
"""
  * * *    i=1
*       *  i=2
*       *  i=3
*       *  i=4
*       *  i=5
*       *  i=6
  * * *    i=7
"""
## OUTER LOOP DECIDES NUMBER OF VALUES IN EACH LINE
for i in range(1,8):
    # INNER LOOP DECIDES NUMBER OF VALUES IN EACH LINE
    for j in range(1,6):
        if i in [1,7]:
            if j in[1,5]:
                print(" ",end=" ")
            else:
                print(j,end=" ")
        elif i in [2,3,4,5,6]:
            if j in [1,5]:
                print(j,end=" ")
            else:
                print(" ",end=" ")
        else:
            print(j,end=" ")
    print()
"""
  2 3 4   
1       5 
1       5 
1       5 
1       5 
1       5 
  2 3 4
"""
print("_"*50)
for i in range(1,8):
    for j in range(1,6):
        if i in [1,7]:
            if j in[1,5]:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        elif i in [2,3,4,5,6]:
            if j in [1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
"""
 * * *   
*       * 
*       * 
*       * 
*       * 
*       * 
  * * *   
"""
print("_"*50)
pt1="*"
pt2=" "
"""
____*____  i=1
___*_*___  i=2
__*****__  i=3
_*_____*_  i=4
*_______*  i=5
"""
for i in range(1,6):
    for j in range(1,10):
        if i==1:
            if j==5:
                print(pt1,end=" ")
            else:
                print(pt2,end=" ")
        elif i==2:
            if j in[4,6]:
                print(pt1,end=" ")
            else:
                print(pt2,end=" ")
        elif i==3:
            if j in[3,4,5,6,7]:
                print(pt1,end=" ")
            else:
                print(pt2,end=" ")
        elif i==4:
            if j in[2,8]:
                print(pt1,end=" ")
            else:
                print(pt2,end=" ")
        elif i==5:
            if j in[1,9]:
                print(pt1,end=" ")
            else:
                print(pt2,end=" ")
    print()
"""
        *         
      *   *       
    * * * * *     
  *           *   
*               * 
"""
print("_"*50)
"""
******
******
  **
  **
  **
  ** 
"""
for i in range(1,7):
    for j in range(1,7):
        if i in [1,2]:
            print("*",end=" ")
        elif i in [3,4,5,6]:
            if j in [3,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
"""
* * * * * * 
* * * * * * 
    * *     
    * *     
    * *     
    * *     
"""

#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end=" ")

# 2). Python Loops program to construct the following pattern, using a nested for loops.
"""
   *
   * *
   * * *
   * * * *
   * * * * *
   * * * *
   * * *
   * *
   *
"""
for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):
    print(i*"*")





