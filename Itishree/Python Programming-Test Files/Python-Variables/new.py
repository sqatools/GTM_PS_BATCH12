a=34
print(a)
print("*"*50)
A = B = C = 200
print("Value of A:",A)
print("Value of B:",B)
print("Value of C:",C)
print("*"*50)
A,B,C=100,200,300
print("value of A",A)
print("value of B",B)
print("value of C",C)
############################
print("*"*50)
A,B,C=100,200,300
print(A,B,C) # 100 200 300
####################OPERATOR##############
#ADDITION OPERATOR#
print("*"*50)
var1 = 30
var2 = 20
print(var1+var2)  # 50
#########
print("*"*50)
print("Addition:",var1+var2) # Addition: 50
output=var1+var2
print(output)  #50
#SUBSTRACTION OPERATOR#
print("*"*50)
var1 = 60
var2 = 40
print(var1-var2)  #20
print("*"*50)
print("Substraction:",var1-var2)  # Substraction: 50
#MULTIPLICATION OPERATOR#
print("*"*50)
var1 = 70
var2 = 40
print(var1*var2)  # 2800
print("*"*50)
print("Multiplication:",var1*var2)  #Multiplication: 2800
#Division OPERATOR#
print("*"*50)
var1 = 50
var2 = 6
print(var1/var2)
print("Division /:",20/2)  # Division /: 10.0 -you can declare the number in print in division
print("*"*50)
print(var1//var2)   # 8 as double divison gives whole number
print("*"*50)
print("Remainder /:",var1/var2) #Remainder /: 8.333333333333334
print("Remainder /:",15%3)  # Remainder /: 0
##Compare Operators-==,!=#####
print("*"*50)
P = 400
Q = 400
R = 600
print(P==Q) # True
print(Q==R) #False
print(R==P) #False

###Get power of Value###
print("*"*50)
a=124
print("square of 124:",a**2) # square of 124: 15376-Here **2(square).
# you can increase number by using ** inorder to get more double of that value means a**5,here a =124;124*5 likewise
print("*"*50)
print("square of 12:",12**2) # square of 12 : 144-Here **2(Square)
print("cube of 7:",7**3) # cube of 7: 343 -Here **3(cube)

##To solve quadratic equation by using above operators##
#(a+b)^2=a^2+b^2+2ab
print("*"*50)
a = 10
b = 2
##can declare in muktiple way to compare between LHS AND RHS##
print((a+b)**2) #144
print("*"*50)
print("Square of a+b:",(a+b)**2) # Square of a+b: 144
print(a**2 + b**2 +2*a*b)
##Another way##
LHS=(a+b)**2
RHS= (a**2 + b**2 +2*a*b)
print(LHS==RHS) # True
print("*"*50)
a = 10
b = 2
c=((10+2)**2)
d=(10**2+2**2+2*10*2)
print (c==d)

#### Python Data Type####

####### Integer ############
var1 = 0
var2 = 156
var3 = 27777778889999
var4 = -3546
print(var1,type(var1)) # 0 <class 'int'>
print("-"*50)
print(var2,type(var2)) # 156 <class 'int'>
print("-"*50)
print(var3,type(var3)) # 27777778889999 <class 'int'>
print("-"*50)
print(var4,type(var4)) # -3546 <class 'int'>
print("-"*50)
####### Pointer ############
var1 = 0.5
var2 = 156.34
var3 = 27777778889999.124
var4 = -3546.23
print(var1,type(var1)) #0.5 <class 'float'>
print("-"*50)
print(var2,type(var2)) #156.34 <class 'float'>
print("-"*50)
print(var3,type(var3)) #27777778889999.125 <class 'float'>
print("-"*50)
print(var4,type(var4)) #-3546.23 <class 'float'>
print("-"*50)
####### Complex  ############
var1 = 5 + 28j # 5 as real number and 28j is imaginary number
print(var1,type(var1))
print("-"*50)
print("real number:", var1.real,type(var1))      #real number: 5.0 <class 'complex'>
print(" imaginary number:", var1.imag,type(var1)) #imaginary number: 28.0 <class 'complex'>
print("-"*50)
# in other way####
var1 = 7 + 125j
print(var1,type(var1))
print("-"*50)
print(var1.real,type(var1)) #7.0 <class 'complex'>
print(var1.imag,type(var1)) #125.0 <class 'complex'>
print("-"*50)
#################
P2 = -90 - 1259j
print(P2,type(P2))
print("-"*50)
print(P2.real,type(P2)) # -90.0 <class 'complex'>
print (P2.imag,type(P2)) #-1259.0 <class 'complex'>
########String################
print("-"*50)
str1 = ''
print(str1,type(str1))  #<class 'str'>
print("-"*50)
S2 = "Hey"
print(S2,type(S2)) # Hey <class 'str'>
print("-"*50)
S3 = """
40 fghhbbbbbbbjbjbjbbbhbhbhbhbhjbhjbhjbhjbhjbhbhbhjbhjbhbhjbhjbhbhjbhjbhbhjbbbbbbbbbbbbbbbbbbbbbbbbbb
hjbjbnbn nnbb """
print(S3,type(S3)) #











