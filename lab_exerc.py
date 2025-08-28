for i in range(1500,2700):
    if i%5 == 0 and i%7 == 0:
        print(i, end=" ")


print("#"*50)

##############################################
for i in range(1,10):
    for j in range(1,5):
        if i in [1,9]:
            if j in [1]:
                print("*", end ="")
            else:
                print(" ", end= " ")
        if i in [2,8]:
            if j in [1,2]:
                print("*", end ="")
            else:
                print(" ", end= " ")
        if i in [3,7]:
            if j in [1,2,3]:
                print("*", end ="")
            else:
                print(" ", end= " ")
        if i in [4,6]:
            if j in [1,2,3,4]:
                print("*", end ="")
            else:
                print(" ", end= " ")
        if i in [5]:
            if j in [1,2,3,4,5]:
                print("*", end ="")
            else:
                print(" ", end= " ")

    print()
##########################################
for i in range(6):
    print(i*"*")
    for i in range(4, -1, -1):
        print(i * "*")

#############################################


