


for i in range(1,8):
    for j in range(1,6):
        if i in [1,7]:
            if j in [1, 5]:
                print(" ", end="")
            else:
                print(j, end="")
        if i in [2,3,4,5,6]:
            if j in [1,2,3,4,5]:
                print(j, end=" ")
            else:
                print(j, end=" ")




    print()



#################################################

for i in range(1,6):
    for j in range(1, 10):
        if i == 1:
            if j == 5:
                print("*", end = "")
            else:
                print("_", end = "")
        if i == 2:
            if j in [4,6]:
                print("*", end="")
            else:
                print("_", end="")
        if i == 3:
            if j in [3,4,5,6,7]:
                print("*", end="")
            else:
                print("_", end="")
        if i == 4:
            if j in [2,3,4,5,6,7,8]:
                print("*", end="")
            else:
                print("_", end="")
        if i == 5:
            if j in [1,9]:
                print("*", end="")
            else:
                print("_", end="")

        print ("_", end=" ")

    print()