#global variable
var_x=100

def function1():
    var_y=200 #local variable
    print("local variable")
    print("gobal variable var_x:",var_x)
    print("local variable var_y:",var_y)

def function2():
    var_z=600 #local variable
    print("global var_x:",var_x)
    print("local variable var_z:",var_z)

function1()
print("_"*50)
function2()
"""
local variable
gobal variable var_x: 100
local variable var_y: 200
__________________________________________________
global var_x: 100
local variable var_z: 600
"""
print("_"*50)
####### non local variable ###
"""
var_p=200
def outer_function():
    var_q=300
    def inner1_fun():
        var_r=400  #local variable
        print("___inner fun1___")
        print("global variable var_p:",var_p)
        print("local variable var_r:",var_r)
        print("non local variable var_q:",var_q)
    def inner2_fun2():
        var_r=400  #local variable
        print("___inner fun2___")
        print("global variable var_p:",var_p)
        print("local variable var_r:",var_r)
        print("non local variable var_q:",var_q)
    inner1_fun()
    inner2_fun2()
"""
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







