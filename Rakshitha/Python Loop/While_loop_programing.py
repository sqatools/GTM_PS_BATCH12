## while condition
  # code
n=1
while n<10:
    print(n)
    n=n+1
"""
1
2
3
4
5
6
7
8
9
"""
#Infinite loop
n=1
while True:
    print(n)
    n=n+1
    if n==1000:
        break
##Write a program to reverse a number with the help of while loop
num=123
rev=0
while num>0:
    temp=num%10
    rev=rev*10+temp
    num=num//10
print("rev output:",rev)
#rev output: 321

#write a program to get fibanacci series
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for _ in range(10):
    a,b=b,a+b
    print(b,end=" ")
# 0 1 1 2 3 5 8 13 21 34 55 89

