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

# overwrite default parameter values
addition_nums(90, 100, 70)
# addition of x: 90, y:100, z: 70 : 260

# addition_nums(4, 6, 8, 20)
# addition_nums() takes from 1 to 3 positional arguments but 4 were given


# HW: Python Function
# 1. write a python function get prime number
# 2. write a python function to print T patter
# 3. write a python function to list of prime number 1 to 100
print("_" * 50)


##########################################################################
# write a python function get factorial of list values:
# Call function inside the function.

def get_factorial_value(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i

    print(f"factorial of: {num} :", fact)


def get_fact_list_values(list1):
    for num in list1:
        # call factorial inside this function
        get_factorial_value(num)


xyz = [3, 5, 6]
get_fact_list_values(list1=xyz)
# get_fact_list_values([3, 5, 6])

print("_" * 40)

###################################################
# specify the data type in the function parameters
tup1 = (3, 4, 5)


def factorial_of_diff_value(values: tuple):
    """
    This function will accept the values from user as tuple of values
    and call get_factorial_value function to get actual output.
    :param values: tuple of values
    :return:
    """
    for v1 in values:
        get_factorial_value(num=v1)


factorial_of_diff_value(values=tup1)
"""
factorial of: 3 : 6
factorial of: 4 : 24
factorial of: 5 : 120

"""

# get doc string of the function
print(factorial_of_diff_value.__doc__)

print("_" * 50)


#############################################
# return value from function
# ->  return statement will stop the execution of the function immediately and return value
def multiplication(n1, n2):
    return n1 * n2


# output = multiplication(4, 5)
# print("output :", output)


def get_sum_of_value(n1, n2):
    sum = 0
    for i in range(n1, n2, 1):
        sum = sum + i

    return sum


result = get_sum_of_value(5, 10)
print("sum value :", result)


# return value on the basis of condition

def return_sum_of_value_with_cond(n1, n2):
    sum = 0
    for i in range(n1, n2, 1):
        print(i)
        sum = sum + i
        if sum > 30:
            return sum


result2 = return_sum_of_value_with_cond(10, 20)
print("result2 :", result2)
"""
10
11
12
result2 : 33
"""

print("_" * 50)


######################
# return multiple value from function
def get_all_math_operations(n1, n2, n3):
    add = n1 + n2
    multi = n2 * n3
    sub = n3 - n1
    return add, multi, sub


result3 = get_all_math_operations(20, 30, 40)
print("result3 :", result3)  # (50, 1200, 20)

a, b, c = get_all_math_operations(40, 50, 60)
print("addition :", a)  # addition : 90
print("multiplication :", b)  # multiplication : 3000
print("division :", c)  # division : 20


# for practice program
# https://sqatools.in/python-function-programs/