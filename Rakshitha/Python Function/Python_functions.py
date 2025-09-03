#coustam functions
def greeting(msg):
    print(msg)
""" def:keyword
    greeting: function name
    msg:parameter which accepts the value
    para msg:
    return:
"""

def addition_values(n1,n2):
    print("Addition:",n1+n2)
greeting("good morning")
greeting("hello we are learning python programing")
print("_"*50)
def addition_values(n1,n2):
    print("Addition:",n1+n2)
#1. pass by value:-when we direct pass the values for the parameters then it is called pass by values
addition_values(30,40)
addition_values(100,200)

#2. pass by reference:- pass value to the parameter with the reference same other variable
x=500
y=400
addition_values(x,y)

#write python function to get functionl of given number
def get_function(num):
    fact=1
    for i in range(num,0,-1):
        print(i)
get_function(6)
"""
6
5
4
3
2
1
"""
print("_"*50)
def get_function(num):
    fact=5
    for i in range(num,0,-1):
        print(i)
        fact=fact*i
get_function(5)
"""
6
5
4
3
2
1
"""
print("_"*50)
def get_factorials(num):
    fact=5
    for i in range(num,0,-1):
        print(i,fact)
        fact=fact*i
    print("fact output:",fact)
get_factorials(5)
"""
5 5
4 25
3 100
2 300
1 600
fact output: 600
"""
fact=1
for i in range(5,0,-1):
    fact=fact*i
    print(i,fact)
print("fact output:",fact)
"""
5 5
4 20
3 60
2 120
1 120
fact output: 120
"""
fact1=1
for i in range(5,0,-1):
    print(i)
    fact1=fact*5
    print(fact1)
"""
5
600
4
600
3
600
2
600
1
600
"""
#function with default parameter values
#default parameter should be always at the end of list of parameter
def addition_nums(x,y=50,z=60):
    print(f"addition of x:{x},y:{y},z:{z}:",x+y+z)
addition_nums(40)
# addition of x:40,y:50,z:60: 150
# default parameter values
addition_nums(30,20)
# addition of x:30,y:20,z:60: 110
#overwrite default parameter value
addition_nums(90,100,70)
# addition of x:90,y:100,z:70: 260
print("_"*50)

#Write a python function get factorial of list values
#call function inside the fuction
def get_factorial_values(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    print(f"factorial of:{num}:",fact)

def get_fact_list_values(list1):
    for num in list1:
        get_factorial_values(num)
list_v=[5,7,9,10]
get_fact_list_values(list_v)
# get_fact_list_values[3,5,6]
"""
factorial of:5: 120                         
factorial of:7: 5040
factorial of:9: 362880
factorial of:10: 3628800
"""
print("_"*50)
#####specify the data type in the function parameter
tup1=(3,4,5)
def factorial_of_diff_value(values:tuple):
    """
    this function will accept the values from use as tuple of values and call get_function_values function to get actual output
    :param values:
    :return:
    """
    for v1 in values:
        get_factorial_values(num=v1)
factorial_of_diff_value(values=tup1)
"""
factorial of:3: 6
factorial of:4: 24
factorial of:5: 120
"""
# get doc string of the function
print(factorial_of_diff_value.__doc__)
"""
this function will accept the values from use as tuple of values and call get_function_values function to get actual output
:param values:
:return:
"""

#### how to get return values from fuction
def multiplication(n1,n2):
    return n1*n2
output=multiplication(4,5)
print("output:",output)
# output: 20

## return statement will stop the excecution of the  function immediately and return value
def multiplication(n1,n2):
    return n1+n2
def get_sum_of_value(n1,n2):
    sum=0
    for i in range(n1,n2,1):
        sum=sum+i
    return sum
result = get_sum_of_value(5,10)
print("sum values:",result)
#sum values: 35

### return values on the basis of condition
def return_sum_of_values_with_condition(n1,n2):
    sum=0
    for i in range(n1,n2,1):
        print(i)
        sum=sum+i
        if sum>30:
            return sum
result2=return_sum_of_values_with_condition(10,20)
print("result2:",result2)
"""
10
11
12
result2: 33
"""

##return multiple values from function
def get_all_math_operations(n1,n2,n3):
    add=n1+n2
    multi=n2*n3
    sub=n3-n1
    return add,multi,sub
result=get_all_math_operations(20,30,40)
print("result:",result)
#result: (50, 1200, 20)

a,b,c=get_all_math_operations(40,50,60)
print("addition:",a)
print("multiplication:",b)
print("division:",c)
"""
addition: 90
multiplication: 3000
division: 20
"""



