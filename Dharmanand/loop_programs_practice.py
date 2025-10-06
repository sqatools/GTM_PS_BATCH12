for i in range(6,1, -1):
    for j in range(1, i+1):
        print("*", end=" ")

    print()


###write a program to print O pattern

for i in range(1,8):
    for j in range(1,6):
        if i ==1:
            if j in [2,5]:
                print("*", end="")
            else:
                print(j)
            print(j)
        print("*",end ="")

    print()

