#write a python function to get factorial of list values:
#call function inside function

def get_factorial_value(num):
    fact = 1
    for i in range(num,0,-1):
        fact=fact * i
        print(i,fact)
    print(f"fact output:{num} ",fact)


def get_fact_list_values(list1):
    for i in list1:
        get_factorial_value(i)
list1=[5]
get_fact_list_values(list1)
#call factorial function inside this function


#specify the data type in function parameters

# function to get output
def fact_of_diff_value(values:tuple):
    """This function will accept the values from user as tuple of values and call get+factorial_value()"""

    for a in values:
        get_factorial_value(a)
tup1=(2,3,4)
fact_of_diff_value(tup1)

print(fact_of_diff_value.__doc__)

###return value from function
# return statement will stop the execution of the function and return the value
def multiplication(n1,n2):
    return n1*n2

output=multiplication(2,4)
print("output:",output)

def get_sum_values(n1,n2):
    sum=0
    for i in range(n1,n2,1):
        sum = sum+i
    return sum
result= get_sum_values(2,5)
print("sum values:", result)

# return value on the basis of condition

def return_sum_values_with_condition(n1,n2):
    sum=0
    for i in range(n1,n2,1):
        sum = sum+i
        if sum > 30:
            return sum

return1 = return_sum_values_with_condition(10,20)
print("return1:", return1)
print("#"*50)


###return multiple value from function


def get_all_math_oeprations(n1,n2,n3):
    add = n1 + n2
    multi = n1 * n3
    sub = n3-n1
    return add, multi, sub

a,b,c = get_all_math_oeprations(10,20,30)
#print("result3:", result3)
print("add:", a)
print("sub:", b)
print("multi: ", c)









#specify teh data type in the funcion parameters



