def greetings(msg):
    print(msg)
#greetings: function name
#msg: parameter which accepts the value

greetings("Hello all")

greetings("learning python")

print("*"*50)

def addition_values(n1,n2):
    print("Addition of values:",n1+n2)
# 1. pass by value - when we direct pass the value for the parmeters, then it's called pass by value.
addition_values(12,13)

#2. Pass by reference: Pass value to the parameter with the reference some other variables.
x= 200
y=300
addition_values(x,y)

