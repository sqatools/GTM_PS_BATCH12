for i in range(1,13):
    for j in range(1,21):
        if i == 1:
            if j in [1,2,3,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==2:
            if j in [1,2,3,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==3:
            if j in [1,2,3,6,9,10,11,16]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==4:
            if j in [1,2,3,9,10,11]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==5:
            if j in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==6:
            if j in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==7:
            if j in [9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==8:
            if j in [6,9,10,11,15,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==9:
            if j in [9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==10:
            if j in [1,2,3,4,5,6,7,8,9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i==11:
            if j in [1,2,3,4,5,6,7,8,9,10,11,18,19,20]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()