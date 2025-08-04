# try to solve this equation
#(a+b)^2=a^2+b^2+2ab
a=5
b=6
LHS=(a+b)**2
RHS=a**2+b**2+2*a*b
print(LHS==RHS)

#(a+b)3=a3+3ab(a+b)+b3
a=5
b=10
LHS=(a+b)*3
RHS=a*3+3*a*b*(a+b)+b*3
print(LHS==RHS)

a=3
b=2
result=a**3+3*a*b*(a+b)+b**3
print("(a+b)^3:",result)

#(a+b)+(a-b)=a^2-b^2
a=3
b=2
result=(a+b)*(a-b)
print("(a^2-b^2:",result)
("_"*50)
#calculate the interst
# a=p(1+rt)
p=1000
r=10
t=2
amount=p*(1+r*t)
print("amountpayable:",amount)

#a=p(1+r/n)^nt
p=1000
r=10
n=2
t=2
amount=p*(1+r/n)**n*t
print("amount payable:",amount)

p = 1000
r = 10
t = 2
n=2
amount = p+(p/r)*t
print("Amount payable: ",amount)



