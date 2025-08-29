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

def fact_of_diff_value(values:tuple):
    for a in values:
        get_factorial_value(a)

fact_of_diff_value([2,3,4])






#specify teh data type in the funcion parameters



