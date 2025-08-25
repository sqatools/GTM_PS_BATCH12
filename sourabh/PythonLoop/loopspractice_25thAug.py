#Python Loops program to count the number of
#even and odd numbers from a series of numbers using python.
#Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

num=(1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = 0
even = 0
for val in num:
    if val%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)

#Write a program that
# prints all the numbers from 0 to 6 except 3 and 6 using python.

n = 0
for i in range(0, 6):
    if i == 0:
        print(i)
        n += 1
    elif i in [3, 6]:
        print(i)
    else:
        continue
