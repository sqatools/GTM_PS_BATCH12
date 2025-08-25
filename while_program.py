n = 1
while n < 10:
    n = n+1
    print(n)
###########
# ###############

n=1
while True:
    n=n+1
    print(n)
    if n== 10:
        break

###############################

#write a program to reverse a number with the help of while loop

num=123

rev = 0

while num > 0:
    temp=num%10
    num=num//10
    rev = rev*10+temp

print(rev)


#####################################

# write a program to geta  fibonacci series

#0 1 1 2 3 5 8 13

a =0
b = 1

for _ in range(10):
    a, b = b, a+b
    print(b)
#################################

#write a python get summation all the list values

list1=[5,7,9,12,45,67]
total=sum(list1)
print(total)