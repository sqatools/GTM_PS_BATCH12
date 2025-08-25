# write a python code to get list of all the prime numbers between 1 to 100.

for num in range(1,100):
    prime = True
    for j in range(2,num):
        if num%j ==0:
            prime = False
            break

    if prime:
        print(num, end="")
    else:
        continue

######################
# write a python program to check two strings are anagram to each other:

s1 = "python"
s2 = "ythonp"
anagram = True

for char in s1:
    if char in s2:
        continue
    else:
       anagram = False
    break

if anagram ==True and len(s1) == len(s2):
    print("These strings are anagram")

