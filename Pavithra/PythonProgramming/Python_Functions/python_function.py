def greeting(msg):
    """
    greeting :  function name
    msg : parameter which accepts the value
    :param msg:
    :return:
    """
    print(msg)


greeting("Good Morning")
greeting("Hello we are Learning Python Programming")


def addition_values(n1, n2):
    print("Addition :", n1 + n2)


# 1. Pass by value :  when we direct pass the value for the parameters, then it is called pass by value
# addition_values(30, 40)
# addition_values(100, 200)

# 2. Pass by reference : Pass value to the parameter with the reference some other variables
x = 500
y = 400
# addition_values(x, y)

print("_" * 50)


##################################
# write python function to get factorial of given number
# 5 = 5*4*3*2*1 : 120

def get_factorials(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i  # 1*5 = 5, 5*4 = 20, 20*3 = 60, 60*2 = 120, 120*1 = 120
        print(i, fact)

    print("fact output :", fact)


# get_factorials(6)
# fact output : 720

print("_" * 50)


################################################
# function with default parameters value
# ->  default parameter should be always at the end of list of parameters.

def addition_nums(x, y=50, z=60):
    print(f"addition of x: {x}, y:{y}, z: {z} :", x + y + z)


addition_nums(40)  # x = 40,  and y, z will consider default value y = 50, z=60
# addition of x: 40, y:50, z: 60 : 150

# overwrite default param value
addition_nums(30, 20)  # x = 30, y = 20, and will consider default z=60
# addition of x: 30, y:20, z: 60 : 110
0
# overwrite default parameter values
addition_nums(90, 100, 70)
# addition of x: 90, y:100, z: 70 : 260

# addition_nums(4, 6, 8, 20)
# addition_nums() takes from 1 to 3 positional arguments but 4 were given


# HW: Python Function
# 1. write a python function get prime number
# 2. write a python function to print T patter
# 3. write a python function to list of prime number 1 to 100
