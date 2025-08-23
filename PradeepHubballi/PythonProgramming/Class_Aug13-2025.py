# Q1: Write a python program to print square of the number if it is divisible by 3 or 7 else print cube



num = int(input("Enter a number: "))

if num % 3 == 0 or num % 7 == 0:
   print("Square:", num ** 2)
else:
   print("Cube:", num ** 3)