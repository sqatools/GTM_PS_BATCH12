for i in range(1,10):
    for j in range(1,10):
        if i ==1:
            if j in [1,5,6,7,8]:
                print("*", end=" ")
            else:
                print(" ", end =" ")
        if i in [2,3,4]:
            if j in [1, 5]:
                 print("*",end=" ")
            else:
                print(" ",end=" ")
        print("",end=" ")
        if i in [5]:
            if j in [1,2,3,4,5,6,7,8,9]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        if i in [6,7,8]:
            if j in [5,9]:
                print("*",end="")
        if i in [9]:
            if j in [1,2,3,4,5,9]:
                print("*",end="")

    print()