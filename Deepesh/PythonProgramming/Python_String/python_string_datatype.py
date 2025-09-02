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
print("_" * 50)

# 1. string concatenation:
result1 = "Hello my name is " + name + " and age is " + str(age) + ", I live in " + city
print("result1 :", result1)
# Hello my name is Rahul and age is 30, I live in Mumbai

# 2. Format method:
result2 = "Hello my name is {} and age is {}, I live in {}".format(name, age, city)
print("result2 :", result2)
# Hello my name is Rahul and age is 30, I live in Mumbai


# 3. f string formatting:
result3 = f"Hello my name is {name} and age is {age}, I live in {city}"
print("result3 :", result3)
# Hello my name is Rahul and age is 30, I live in Mumbai

print("_" * 50)
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
print(str_len)  # 11

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
print("_" * 50)
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
print(str4[3])  # r
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
print(s5[-10:-2])  # ing Pyth

# exclude first and last and print every thing else
print(s5[1:-1])  # earning Pytho

# default start value zero
s6 = "Good Morning"
print(s6[:4])  # Good

# default end value is end of string.
print(s6[5:])  # Morning
print(s6[5: len(s6)])  # Morning

# Q1 :
# s1 = "Hello Python Programming"
# output  = "Programming Hello Python"

print("_" * 40)
############################
# Rule2 : str[start index:  end index:  step value]
"""
->  The output will include start index value and exclude end index value.
->  start index, index index and step value could be +ve and -ve.
->  default start value is zero (0), when step value is +ve.
->  default start value is -1, when step value is -ve.
->  default end index value is end of string, when step value is +ve
->  default end index value is start of string, when the step value is -ve


"""
str2 = "Playing Cricket"
print(str2[0:7:1])  # Playing

# print all alternate character from given string
print(str2[0::2])  # PaigCikt

# get a word 'Cricket' in reverse order
print(str2[-1:-10:-1])  # tekcirC g
print(str2[-1:10:-1])  # tekc

# reverse the entire string
print(str2[::-1])  # tekcirC gniyalP
print(str2[-1:-len(str2) - 1: -1])  # tekcirC gniyalP

print(str2[::1])  # Playing Cricket
print(str2[0:len(str2):1])  # Playing Cricket

str3 = "Programming Language"
print(str3[0:12:1])  # Programming

print(str3[12:20:1])  # Language
print(str3[12::1])  # Language
print(str3[-8::1])  # Language
print(str3[12])  # L

print("_" * 50)
################################ String Methods ########################
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
'zfill'
"""

print("_" * 50)
#############
# upper(), lower() :  These method convert the given string from lower to upper and upper to lower case.

str3 = "Learning Python"
print("Upper case result :", str3.upper())  # LEARNING PYTHON
print("lower case result :", str3.lower())  # learning python

print("_" * 50)
########################
# isupper() :  This method check given string is in upper case
# islower() :  This method check the given string is in lower case
s1 = "PYTHON"
s2 = "Programming"
s3 = "learning"
print("s1 is upper :", s1.isupper())  # True
print("s3 is lower :", s3.islower())  # True
print("s2 is upper or lower :", s2.isupper(), s2.islower())  # False False

print("_" * 50)
########################
# swapcase method : This method convert the string characters from lower to upper and upper to lower
str4 = "Very GOOD Morning"
print("swap case result :", str4.swapcase())
#  vERY good mORNING

print("_" * 50)
########################
# title method :  This method convert a normal into title case, it means first letter each word will be capital.
str5 = "india is best cricket team in the world"
print("title result :", str5.title())
# India Is Best Cricket Team In The World

# istitle() : this method return True or False result as per title string rules.
str6 = "Hello Very Good Evening"
str7 = "python is easy to learn"
print("str6 istitle result :", str6.istitle())  # True
print("str7 istitle result :", str7.istitle())  # False

print("_" * 50)
#################################################################
# write a python program to remove duplicate character from given string.
str7 = "Hello We are learning Python"
result = ""

for char in str7:
    print(char)
    if char not in result:
        result = result + char
    else:
        continue

print("result :", result)  # Helo WarnigPyth

# Homework :
# str = "India is great country"
# output = "InDIA IS Great CountrY"

# Q1 :
# s1 = "Hello Python Programming"
# output  = "Programming Hello Python"
