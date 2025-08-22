print("_" * 50)
"""
****____**********  i =1
****----**********  i =2
****----***-------  i =3
****----***-------  i =4
******************  i=5
******************  i=6
--------***----***  i=7 
--------***----***  i=8
***********----***  i=9
***********----***  i=10 
"""
pt1 = "*"
pt2 = " "
for i in range(1, 11):
    for j in range(1, 19):
        if i == 1:
            if j in [1,2,3,4,9,10,11,12,13,14,15,16,17,18]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i == 2:
            if j in [1,2,3,4,9,10,11,12,13,14,15,16,17,18]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")

        elif i == 3:
            if j in [1,2,3,4,9,10,11]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")

        elif i == 4:
            if j in [1,2,3,4,9,10,11]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i == 5:
            if j in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i == 6:
            if j in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                print(pt1, end=" ")
            else:
                    print(pt2, end=" ")
        elif i == 7:
            if j in [9,10,11,15,16,17,18]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i == 8:
            if j in [9,10,11,15,16,17,18]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        elif i in [9, 10]:
            if j in [1,2,3,4,5,6,7,8,9,10,11,15,16,17,18]:
                print(pt1, end=" ")
            else:
                print(pt2, end=" ")
        else:
            print("_", end=" ")

    print()  # This print statement help us to move to next line with default value \n
