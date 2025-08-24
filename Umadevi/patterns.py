#writr a python code to get a list of all the prime number 1 to 100

for Num in range (1,100):
    prime= True

    for j in range (2,Num):

        if Num %j ==0:
            prime=False
            break
            if prime:
                print(Num)

            else:
                continue


#write a python code program to check two string are anagram comapre thechar are same

s1= "python"
s2="yohtnp"
is_same = True

for char in s1:
    if char in s2:
        continue

    else:
        is_same =False

        if is_same == True and len(s1) == len(s2):
            print("char are same")

        else :
            print("char are not  same")


