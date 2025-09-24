# Exception : exception handling allow us to manage custom error message using try and except.

def exception_handling(n1, n2):
    try:
        add = n1 + n2
        print("addition of values :", add)
    except Exception as e:
        print(e)
        print("Can not add integer with string")

#exception_handling(40, 'Hello')
# print("Good morning")

"""
unsupported operand type(s) for +: 'int' and 'str'
Can not add integer with string
"""
################## Raise exeception explicitly #########################

def exception_handling_with_raise(n1, n2):
    try:
        add = n1 + n2
        print("addition of values :", add)
    except Exception as e:
        print(e)
        print("Can not add integer with string")
        raise


#exception_handling_with_raise(30, 'Hello')
# print("Good Morning")

"""
Can not add integer with string
Traceback (most recent call last):
  File "E:\Trainings\GTM_PS_Batch12_July25\GTM_PS_BATCH12\Deepesh\PythonProgramming\ExceptionHandling\exception_handling.py", line 30, in <module>
    exception_handling_with_raise(30, 'Hello')
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "E:\Trainings\GTM_PS_Batch12_July25\GTM_PS_BATCH12\Deepesh\PythonProgramming\ExceptionHandling\exception_handling.py", line 22, in exception_handling_with_raise
    add = n1 + n2
          ~~~^~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'


"""

################## try - except - else #########################

def try_except_else(n1, n2):
    try:
        add = n1 + n2
        print("addition of values :", add)
    except Exception as e:
        print(e)
        print("Can not add integer with string")
    else:
        # else block of code only executes when there is no exception
        print("Code execution is successful")


#try_except_else(40, 100)
"""
addition of values : 140
Code execution is successful
"""

#try_except_else(40, 'Python')
"""
unsupported operand type(s) for +: 'int' and 'str'
Can not add integer with string
"""


################## try - except - else - finally #########################

def try_except_else_finally(n1, n2):
    try:
        add = n1 + n2
        print("addition of values :", add)
    except Exception as e:
        print(e)
        print("Can not add integer with string")
    else:
        # else block of code only executes when there is no exception
        print("Code execution is successful")

    finally:
        # finally block will always execute even there is exception  or no exception.
        print("data cleaning task is done")
        for i in range(1, 5):
            print(i, i**2)


#try_except_else_finally(100, 200)
"""
addition of values : 300
Code execution is successful
data cleaning task is done
1 1
2 4
3 9
4 16

"""

#try_except_else_finally(100, 'Hello')
"""
unsupported operand type(s) for +: 'int' and 'str'
Can not add integer with string
data cleaning task is done
1 1
2 4
3 9
4 16
"""


################## Nested exception #########################

def nested_exception_handling(n1, n2, n3):
    try:
        # outer code
        add = n1 + n2
        print("addition of values :", add)
        try:
            # inner code
            division = n2//n3
            print("Division output :", division)
        except Exception as e2:
            print("e2:", e2)
            print("Can not divide value with zero")
    except Exception as e1:
        print("e1:", e1)
        print("Can not add integer with string")


# fail in outer exception
# nested_exception_handling(20, 'Hello', 50)
"""
e1: unsupported operand type(s) for +: 'int' and 'str'
Can not add integer with string
"""


# fail in inner exception
#nested_exception_handling(20, 80, 0)
"""
addition of values : 100
e2: integer division or modulo by zero
Can not divide value with zero
"""


################## multiple exception #########################

def handle_multiple_exception(n1, n2, n3):
    try:
        add = n1 + n2
        print("addition of values :", add)
        div = n2//n3
        print("division :", div)
        assert n2 == n3

    except TypeError:
        print("Can not add int with string")
    except ZeroDivisionError:
        print("Can not divide number by zero")
    except AssertionError:
        print("Both values are not equal")
    except Exception as e:
        raise e


#handle_multiple_exception(30, 50, 5)

