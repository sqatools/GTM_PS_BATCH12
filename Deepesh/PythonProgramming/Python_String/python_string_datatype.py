"""
# Properties:
->  string is immutable data type.
->  we can define string with single/double/triple quotes.
->  string follows positive and negative indexing.
->  string can contain any type of data as raw string.
"""

str1 = "Hello we are Learning \n Python \t\t\t Programming"
# \n : next line
# \t : tab space
print(str1)

# convert entire string in raw string
str2 = r"Hello we are Learning \n Python \t\t\t Programming"
print(str2)
# Hello we are Learning \n Python \t\t\t Programming

################################# String Formatting ##############
name = "Rahul"
age = 30
city = "Mumbai"
# Hello my name is Rahul and age is 30, I live in Mumbai.
print("_"*50)

# 1. string concatenation:
result1 = "Hello my name is "+name+" and age is "+str(age)+", I live in "+city
print("result1 :", result1)
# Hello my name is Rahul and age is 30, I live in Mumbai

# 2. Format method:
result2 = "Hello my name is {} and age is {}, I live in {}".format(name, age, city)
print("result2 :", result2)
# Hello my name is Rahul and age is 30, I live in Mumbai


#3. f string formatting:
result3 = f"Hello my name is {name} and age is {age}, I live in {city}"
print("result3 :", result3)
# Hello my name is Rahul and age is 30, I live in Mumbai

print("_"*50)
###########################################
# apply loop on string values

s2 = "Programming"
# loop without indexing :  when we apply loop it will print each character one by one
for val in s2:
    print(val, end=" ")
# P r o g r a m m i n g


print()
# loop with indexing
str_len = len(s2)
print(str_len) # 11

for i in range(str_len):
    print(i, s2[i])

"""
0 P
1 r
2 o
3 g
4 r
5 a
6 m
7 m
8 i
9 n
10 g
"""
print("_"*50)
#############################################
# write a python program to get count of total vowels in the string.
s3 = "Very good morning, Hope you are doing good"
vowels = "aeiou"
vowel_count = 0

for char in s3:
    if char in vowels:
        print(char)
        vowel_count = vowel_count + 1
    else:
        continue


print("All vowels count :", vowel_count)
###########################

"""
0   1   2  3   4   +ve  indexing
H   e   l  l   o
-5 -4  -3  -2  -1  -ve indexing

"""

################################### string slicing ########################
str4 = "Learning Python"
print(str4[3])   # r
print(str4[-4])  # t

# slicing help us to get partial string value from long string with the help of index position.

# Rule1 : str[start_index : end_index]
"""
->  In this rule we will the get the output value from left to right
->  Default step value is 1
->  Output will include start index and exclude last index value
->  start index or end index both could be +ve or -ve
->  default start value is zero (0)
->  default end value is end of the string.

"""


# In this rule we will the get the output value from left to right
s5 = "Learning Python"
print(s5[0:8])  # Learning

# start index +ve and end_index as -ve
print(s5[2:-2])  # arning Pyth

# start index -ve and end_index as +ve
print(s5[-6:15])  # Python
print(s5[9:15])  # Python

# start_index -ve and end_index -ve
print(s5[-10:-2]) # ing Pyth

# exclude first and last and print every thing else
print(s5[1:-1])  # earning Pytho


# default start value zero
s6 = "Good Morning"
print(s6[:4])  # Good

# default end value is end of string.
print(s6[5:]) # Morning
print(s6[5: len(s6)])  # Morning


# Q1 :
# s1 = "Hello Python Programming"
# output  = "Programming Hello Python"