var_x = 100


def function1():
    var_y = 200
    print("blabal vriable of Var_X:", var_x)
    print("global variable of var_y:", var_y)

def function2():
    var_z=300
    print("blabal vriable of Var_X:", var_x)
    print("global variable of var_y:", var_z)

function1()
print("_"*60)
function2()