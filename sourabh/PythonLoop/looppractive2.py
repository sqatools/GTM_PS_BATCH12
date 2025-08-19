# write a program to check given number is prime or not,

num=3
prime=True
for val in range(2,num):
    if num % val == 0:
        prime = False
        break
    if prime:
        print("this is prime numeber:", num)
    else:
        print("this is not prime number: ", num)