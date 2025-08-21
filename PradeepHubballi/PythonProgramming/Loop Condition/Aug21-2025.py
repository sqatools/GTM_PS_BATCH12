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
