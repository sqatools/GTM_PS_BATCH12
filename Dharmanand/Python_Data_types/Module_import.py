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






