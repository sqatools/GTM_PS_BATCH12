def get_factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        print(i)
        fact = fact * i
        print("factorial:", fact)


get_factorial(45)
