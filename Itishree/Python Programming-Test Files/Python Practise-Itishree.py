rows=5
for i in range(1,rows+1):
    print('*'*i)

a=5
b=7
print(a)       #5
print(a, id(a))  #5:140717963363368
print("*"*50)
#a=vairable;
#=-Assignment operator
#10-Value to assign Variable
###If Multiple Variable has SAME Values,Address is also Same ###
a=70
b=70
print(a,":",id(a))  #70 : 140717963365448
print(b,":",id(b))  #70 : 140717963365448
print("*"*50)
###ASSIGN SINGKE VALUE TO MULTIPLE VARIABLE ###
a = b = c = 200
print(a,":",a) #200:200
a = b = c = 200
print("Value of a:",a)  #Value of a: 200
print("Value of b:",b)  #Value of b: 200
print("Value of c:",c)  #Value of c: 200
###ASSIGN SINGKE VALUE TO MULTIPLE VARIABLE ###
A = B = C = 200
print("Value of A:",a) #Value of A: 200
print("Value of B:",b) #Value of B: 200
print("Value of C:",c) #Value of C: 200
#print("*"*50)#

a = b = C = 200
print("Value of A:",a)
print("Value of B:",b)
print("Value of C:",c)
#
#Value of A: 200
#Value of B: 200
#Value of C: 200
#CASE SENSITIVE HOW YOU DECLARE THE VARIABLES AND CALLED IT
print("*"*50)
D = E = 900
print("Value of D:",D)
print("Value of E:",E)
print("*"*50)
#############
A = B = C = 200
print("Value of A:",a)
print("Value of B:",b)
print("Value of C:",c)
print("*"*50)
###########
D = E = 900
print("Value of D:",D)
print("Value of E:",E)
############################
print("*"*50)
F = G = 1000
print("Value of F:",F)
print("Value of G:",G)
##########################
print("*"*50)
NAME="Alice"
name="don"
print(NAME)
print(name)
print("*"*50)
########DIFFERENT VARIABLE TO DIFFERENT VALUE##########
A,B,C=100,200,300
print("value of A",A)  #value of A 100
print("value of B",B)  #value of B 200
print("value of C",C)  #value of C 300

print("*"*50)



