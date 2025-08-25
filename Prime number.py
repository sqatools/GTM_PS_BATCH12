# write a python code to get list of all the prime numbers between 1 to 100.

for num in range(1,100):
    prime = True
    for j in range(2, num):
        if num%j == 0:
            prime = False
            break

    if prime:
        print(num)
    else:
        continue
