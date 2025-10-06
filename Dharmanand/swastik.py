for i in range(1,13):
    for j in range(1,21):
        if i in [1]:
            if j in [1,2,3,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*", end =" ")
            else:
                print("", end =" ")
        if i in [2]:
            if j in [1,2,3,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*", end =" ")
            else:
                print("", end =" ")
        if i in [3]:
            if j in [1,2,3,9,10,11]:
                print("*", end=" ")
            else:
                print(" ",end = " ")
        if i in [4]:
            if j in [1,2,3,9,10,11]:
                print("*", end=" ")
            else:
                print(" ",end = " ")

    print("")