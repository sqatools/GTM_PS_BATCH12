a=10
# a:variable
# =:assingment
# 10:data or value of assing variable
print(a, id(a)) #10 140708911269064

a=11
print(a, id(a)) #11 140708911269096

a=10
print(a,id(a))
print("_"*50)
##### If multiply variable have same value then their address is same #####
p=50
q=50
print(p, ":" ,id(p))
print(q, ":", id(q))

print("_"*50)
##### Assign single value to multiple variables ######
x=y=z=100
print("value of x:", x)
print("value of y:", y)
print("value of z:", z)

print("_"*50)
##### Assign different value to different variables #####
A,B,C=50,100,200
print("value of A:", A)
print("value of B:", B)
print("value of C:", C)

print("_"*50)
# There are 5 Rules to define variable name:-
# 1. There should not be space in variable name
#var a=50 #invalid
#var_a=50 #valid

# 2. There is no limit for variable name length
w=10 #valid
hello_we_are_learning_python_programing=500 #valid

# 3. variable names can't start with names
# 123_var=700 #invalid
var_123=800 #valid

# 4. variables name should not contain special character in the except_
# var&123=600 #invalid
# var*abc=700 #invalid

# 5. Variable name are case-sensitive
name='rahul'
Name='manoj'
nAme='mohit'
NAME='JOHAN'
print(name, "|", Name, "|", nAme, "|", NAME)

print("_"*50)
## Mathematical operations ##
# +:add
# -:minus
# *:multiply
# /:division with single /
# //:division with double //
# %:remainder operator
# ==:equal to operator
# **:power operator

var1=50
var2=6
print("Addition :", var1+var2)
output=var1+var2
print("output :", output)
print(output)
print("subtraction :", var1-var2)
print("multiplication :", var1*var2)
print("division with / :", 15/2)
print("division with // :", var1//3)
print("remainder value :", 15%4)

print("_"*50)
# Get power of value
print("square of 5 :", 5**2)
print("cube of 12 :", 12**3)

print("_"*50)
# try to solve this equation
#(a+b)^2=a^2+b^2+2ab
a=5
b=6
LHS=(a+b)**2
RHS=a**2+b**2+2*a*b
print(LHS==RHS)

