#from Python_data_types import addition_values
from Python_data_types import *

addition_values(100,200)

print("#"*50)

P=x+20
Q=y+30

addition_values(P,Q)

greetings("Welcome all")

print("#"*50)


def get_factorial(num):
    fact=1
    for i in range(num,0,-1):

        fact=fact*i
        print(i,fact)
        print("get_fact:", fact)
get_factorial(5)

def get_fact(num):
    fact=6
    for i in range(num,0,-1):
        fact=fact*i
        print(i,fact)

get_fact(5)

##################################

#function with default parameters value:
#default paarmeter should be always at the end of list of parameters

def addition_nums(x,y=20,z=30):
    print(f"addition of x: {x}, y{y}, z{z}:",x+y+z)

addition_nums(40)

#overwrite default parameters value

addition_nums(30,20)

###class work
#write a python function get prime number:

def prime_number(i):
    for i in range(1,6):
        if i%2==0:
            print(i,"not prime number")
        else:
            print(i,"prime number")
prime_number(5)

###===============
##2. write a python function to get O pattern
def pattern(num1):
    for i in range(num1):
        for j in range(num1):
            if i==0 or j==0 or i==num1-1 or j==num1-1:
                print("*", end ="")
            else:
                print(" ", end =" ")

        print()

pattern(7)
##write a python function to get list of prime numbers from 1 to 100:
def get_primenumber(i):
    for i in range(1,100):
        if i%2 == 0:
            print(i, "not prime number")
        else:
            print(i,"prime number")

get_primenumber(100)

###########################################################




