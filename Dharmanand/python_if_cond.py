#compare 2 values with if condition

a = 40
b= 30
print (a==b)

if a==b:
    print("values are equal")
else:
    print("values are not equal")

print("#"*50)
###########take value as input from user
###user has to convert the data type as his requirement

num = input("Enter the num value: ")

print ("#"*50)


print(num, type(num))


###################################################
# check given no. is odd or even

rate = int(input("Enter the value of rate:"))


if (rate)%2 == 0:
    print("rate is even:",rate)
else:
    print("rate is odd:",rate)

    print("#"*50)

##write a python program to check given no. is divisible by 3 or 5

val1 = int(input("Enter the values of val1:"))

if (val1)%3 ==0 and (val1)%5 ==0:
    print ("val1 is divisible by 3 and 5 :", val1)
else:
    print("val1 is not divisible by 3 and 5: ",val1)

    print("#"*50)

j = 18

if j%3 ==0 or j%5 ==0:
    print("j is divisble by 3 and 5:",j)
else:
    print("j is not divisble by 3 and 5:",j)


    print("*"*50)

####### write a python program to find the maximum value among three numbers

a=30
b=20
c=30

if a > b and a >c:
    print("a has greater value:",a)
elif b > a and b >c:
    print("b has greater value",b)
elif c > a and c > b:
    print("c has greater value",c)
else:
    print(" no one has greater value")

print("#"*50)
##CLASS WORK
print("#"*50)

#k > 30 < 50 #third class
#k>50 and k<60 # second class
#k>60 and k<100 # first class

k= int(input("Enter marks of student:"))

if k > 30 and k < 50:
    print("k is third class :", k)
elif k > 50 and k <60:
    print("k is second class :", k)
elif k > 60 and k < 100:
    print(" k is first class:",k)
elif k < 30:
    print(" failed in exam")
elif k > 100:
    print("Input is invalid")
else:
    print ("No result ")

age = int(input("Enter age of a Voter"))

if age >= 18:
    print("Eligible for vote")
else:
    print("not eligible for voting")


print("#"*50)

h = 14

if h%7==0 or h%11==0:
    print("h is divisible by 7 and 11:",h)
else:
    print("h is not divisible by 7 and 11:", h)








