for i in range(1, 6):
    for j in range(1, 10):
        if i == 1:
            if j == 5:
                print("*", end=" ")
            else:
                print("_", end=" ")
        elif i == 2:
            if j in [4, 6]:
                print("*", end=" ")
            else:
                print("_", end=" ")

        elif i == 3:
            if j in [3, 4, 5, 6, 7]:
                print("*", end=" ")
            else:
                print("_", end=" ")

        elif i == 4:
            if j in [2, 8]:
                print("*", end=" ")
            else:
                print("_", end=" ")

        elif i == 5:
            if j in [1, 9]:
                print("*", end=" ")
            else:
                print("_", end=" ")
print()