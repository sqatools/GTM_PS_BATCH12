"""
global variable:  If we define any variable outside the function, then it is called global variable
local variable:  If we define any variable inside the function, then it is called local variable.
non-local variable : non variable is global for all the inner function, and its scope is limited to the outer function only
                     can not use outside of outer function.
"""
# global variable
var_x = 100

def function1():
    global var_x
    var_y = 200 # local variable
    var_x = 300
    print("local variable")
    print("global variable  var_x :", var_x)
    print("local variable var_y :", var_y)


def function2():
    var_z = 600 # local variable
    print("global variable  var_x :", var_x)
    print("local variable var_z :", var_z)


function1()
print("_"*50)
function2()



print("_"*50)
#################################################
var_p = 200

def outer_function():
    var_q = 300 # non-local variable for all the inner methods.

    def inner1_fun():
        global var_p
        nonlocal var_q
        var_r = 400 # local variable
        var_p = 800
        var_q = 900
        print("---inner fun1---")
        print("global variable var_p:", var_p)
        print("local variable var_r:", var_r)
        print("non local variable var_q:", var_q)

    def inner1_fun2():
        var_s = 400
        print("---inner fun2---")
        print("global variable var_p:", var_p)
        print("local variable var_s:", var_s)
        print("non local variable var_q :", var_q)



    inner1_fun2()
    print("_"*50)
    inner1_fun()
    print("_" * 50)
    inner1_fun2()



outer_function()





####################################################################