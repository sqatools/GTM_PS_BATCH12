# compare 2 value


"""
synatx:

if cond:
    code

else:
    code

"""

#a1,b =10,7
a1,b=10,10
print(a1 == b) #this also finr
if a1 == b:
    print("value are true")
else:
    print("value are false")

print("/"*1000)

#Taking input from the user on terminal

val=input("Enter the value u want to check:")
print(val,type(val))


print("/"*1000)


#check the no is even or odd

#Logic:-
#(num)%2 ==0:
num=input("enter the number:")

if int(num)%2==0 and int(num)%3==0:
    print("its even") #it chceks the value which is accepted at fisrt it will print first FIFO
else:
    print("its odd")

    num1 = input("enter the number")

    if int(num1) % 2 == 0 | int(num1) % 3 == 0:
        print("its even")  # it chceks the value which is accepted at fisrt it will print first FIFO
    else:
        print("its odd")
    print("/" * 1000)
    # 1. writr a python probolen  divisible by 3 nd 5


number=input("enter the number check")

if int(num)%2==0 and int(num)%3==0:
    print("its divisible by 3 nd 5")
else:
    print("its divisible by 3 nd 5")

    #syntax for elif
"""
#elif cond

if cond1:
    code
elif code2:
    code
elif code3:
    code
"""


#write a python pbl max val among thre number
a=10
b=60
c=80
if a>b and a>c:
    print("a is > value:",a)
elif b>a and c>a:
    print("a is > value:", a)
else:
    print("no one has lesser value")

#practice session -prgm 1

marks =int(input("enter the students marks for show the result:::::"))

if marks >30 and marks <50:
    print("passed with 3rd grade")
elif marks > 50 and marks < 60:
    print("passed with 2rd grade")
elif marks > 60 and marks < 70:
    print("passed with 1st grade")
elif marks > 70 and marks < 80:
    print("passed with excellent performance")
elif marks > 80:
    print("passed with super of excellent performance")

else:
    print ("less that 30 is failed continue again")
#enter the students marks for show the result::::: 81
#passed with super of excellent performance


#2.write a python program is checjk the elligible for vote

age= int(input("Enter Your age:"))

if age>=18 :print("The person is elligible to vote")
elif age<18 : print("wait for reach after 17 age is vote grow grow grow")

#3. write a prgrm for check the numbers divisible by 7 and 11

qwert=int(input("enter the number"))

if int(qwert)%7 ==0 and int(qwert)%11 ==0:
    print("Number is divisible by 7 and 11")

else:
    print("cannot baby")
    #August 12 class is not happend
#August 13 th

#Nested If condition > one condition is dependent on another condition
"""
if cond1:
    code
else:
    code

#nested if else
if cond1:
    code

    if cond2:
        code
    else:
7        code
     #    this 137 to 140 is  checks the condition depends on only the cond 1   if its cond 1 is  pass it will go to check the cond 2 or starts itself false it wont go into th cond2 itself
else:
    code


"""
#Write a python code to describe the interview process with help of nested if condition
Round1="pass"
Round2="pass"
Round3="pass"


if Round1=="pass":
    print("congrats uma r u pass")

    #If uma pass she will go to next round for attend the interview process or else she will go to home

    if Round2=="pass":

        print("uma cracked 2 also")
        if Round3=="pass":

            print("Uma is selected in TCS with 10 lakhs package")
    else:
        print("we can do it try again uma better work hard next do logically code")

print("/"*1000)

#single line of if condition
var=21
output ="even" if var%2==0 else "odd"
print("output:",output)
print("/"*1000)

# python code to check gn val is available in the list

V1 =13
list=[12,13,16,12,8,12]
what= True if V1 in list else False
print("Results:",what)

print("/"*1000)


#1. write a python program to print sqaure of the number if it divible by 3 or 7 else print cube

input=int(input("Enter the number"))

if int(input)%3 ==0 or int(input)%7 ==0:
    print("Its divisible")
    print("results",input**2)
else :
    print("results",input**3)
    print("Its Not divisible")

#2.
#doubyt - 2 question
#August 14th
#LOOP

#For is a keyword for loop in means (it)> will look

List=[2,7,6,8,9,6]

for result in List:
    #print(result)
    print("indexof",List[1]) #to avoid execiting will go for range


    #Range
#syntax
#range(start,end,step)function.
#Range output includes start and exclude the end value
#Range (1,9,1)>> 1,2,3,4,5,,6,7,8

for i in range (1,10,1):
    print (i)


#1. print all odd vale from 1 to 20

for i in range (1,20,1):
    print (i)

#write apython program to add all the value 1 to 10
sum=0
for var in range (2,20,2): #(1, 2,3,4,5,,6,7,8,9,10)
    sum =sum +var #0+1=1(sum value is this), 1+2=3 ,3+3=6, 6+4=10..............adding the total with range
    print("addition:",sum)

mul =1
for va in range (1,15):
    mul= mul * va
    print("multi:",mul)



#August 15 is not class happened


#August 18th

#next line end=""



#Use if condition inside for-loop

#1to 100 which is divisble by 7

for o in range (1,100):

    if o%7==0:
        print(o)

#program for even or odd  from 1to 20

for u in range(1,20):
    if u%2==0:
        print("its even")

    else:
        print("its odd")


#Nested For-LOOP
#write a program to check given number is prime or not
"""
nest= 9
prime = True
for A in range (2,nest):
    if nest%A ==0:
        prime=False
if prime :
    print("this is prime,",nest)

"""

for K in range (1,6):
    for b in range(1,4):
        print(K)