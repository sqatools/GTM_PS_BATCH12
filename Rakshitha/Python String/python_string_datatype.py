#python string data types

str1="hello we are learning \n python \t\t\t programming"
# \n:next line
# \n:tab space
print(str1)
# hello we are learning
#  python 			 programming

str2=r"hello we are learning \n python \t\t\t programming"
print(str2)
# hello we are learning \n python \t\t\t programming
print("_"*50)
### string formating #########
name='rahul'
age=30
city="mumbai"
##string concatenation#####
result1="hello my name is "+name+" and age is"+str(age)+",I live in "+city
print("result1:",result1)
# result1: hello my name is rahul and age is30,I live in mumbai

##formate method
result2="hello my name is {} and age is {}, I live in{}" .format(name,age,city)
print("result2:",result2)
# result2: hello my name is rahul and age is 30, I live in mumbai

## f string formating:
result3="hello my name is{name} and age is {age}, I live in {city}"
print("result3:",result3)
# result3: hello my name is{name} and age is {age}, I live in {city}
print("_"*50)
## Applyning loop on string values
s2="programming"
#loop without indexing:when we apply loop it will print each character one by one
for val in s2:
    print(val,end=" ")
#p r o g r a m m i n g
print("_"*50)
## loop with indexing
str_len=len(s2)
print(str_len) #11

for i in range(str_len):
    print(i,s2[i])
"""
0 p
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
## write a python program to get count of table vowels in the string
s3="very good morning, hope you are doing good"
vowels="aeiou"
vowels_count=0

for char in s3:
    if char in vowels:
        print(char)
        vowels_count=vowels_count+1 # All vowels count: 15

    else:
        continue
print("All vowels count:",vowels_count)
"""
e
o
o
o
i
o
e
o
u
a
e
o
i
o
o
All vowels count: 15
"""
print("_"*50)
"""
 0 1 2 3 4  +ve indexing
 h e l l o
-5-4-3-2-1  -ve indexing
"""
##string slicing
str4="learning python"
print(str4[3])  #r
print(str4[-4]) #t

#slicing help us to get partial string values from long string with the help of index position

#Rule1:str[start_index:end_index]
##In this rule we will the output value from left to right
s5="learning python"
print(s5[0:8])  #learning

#start index +ve and -ve index as -ve
print(s5[2:-2])  #arning pyth

##start index -ve and +ve index as +ve
print(s5[-6:15])  #python
print(s5[9:15])   #python

##start index -ve and +ve index  -ve
print(s5[-10:-2])  #ing pyth

#excluded first and last and print every thing else
print(s5[1:-1])   #earning pytho

#default start value zero
s6="good morning"
print(s6[:4])  #good

#default end value is end of sting
print(s6[5:])         #morning
print(s6[5:len(s6)])  #morning
print("_"*50)
##rule2: str[start index:end index:step value]
str2="playing cricket"
print(str2[0:7:1])  #playing

#print all atternate charater from given string
print(str2[0::2])  #paigcikt

#get a word 'cricket' in revers order
print(str2[-1:-8:-1]) #tekcirc
print(str2[-1:-10:-1]) #tekcirc g
print(str2[-1:10:-1]) #tekc

##reverse the entire string
print(str2[::-1]) #tekcirc gniyalp
print(str2[-1:-len(str2)-1:-1])  #tekcirc gniyalp

str3="programming language"
print(str3[0:12:1]) #programming
print(str3[12:20:1])  #language
print(str3[12::1])  #language
print(str3[-8::1])   #language
print(str3[12])      #l
print("_"*50)
############### String method #####
# upper(),lower(): these method convert the given string from lower to upper and upper to lower case.
str3="learning python"
print("upper case result:", str3.upper())  #upper case result: LEARNING PYTHON
print("lower case result:", str3.lower())  #lower case result: learning python

#isupper():This method check given string is in upper case
#islower():This method check the given string is in lower case
s1="PYTHON"
s2="programming"
s3="learning"
print("s1 is upper:",s1.isupper())
print("s3 is lower:",s3.islower())
print("s2 is upper or lower:",s2.isupper(),s2.isupper())
"""
s1 is upper : True
s3 is lower : True
s2 is upper or lower : False False
"""
print("_"*50)
#swapcase method: this method covert the string character from to upper and lower
str4="very GOOD Morning"
print("swap case result:", str4.swapcase())
# swap case result: VERY good mORNING

#title method:this method convert a normal into title case it means first letter each word will be capital
str5="India is best cricket team is the world"
print("title result :", str5.title())
# title result : India Is Best Cricket Team Is The World

#istitle(): this method return true or false result as per title string rules.
str6="Hello Very Good Evening"
str7="Python is easy to learn"
print("str6 istitle result:",str6.istitle())  #True
print("str7 istitle result:",str7.istitle())  #False

#write a python to remove duplicate character from give string
str7="Hello we are learning Python"
result=""
for char in str7:
    print(char)
    if char not in result:
        result=result+char
    else:
        continue
print("result:", result) #result: Helo warnigPyth

#count method:- this count method the number of occurences of any charater or subrting inthe target string

str_a="learning python is fun, and very good morning"
#get count of i charater
print("count of i:",str_a.count('i'))
# count of i: 3

#count of substring ing
print("count if ing substring:",str_a.count('ing'))
# count if ing substring: 2

#programming to get count of each charater
str_b="python programming"
for char in str_b:
    print(char,":",str_b.count(char))
print("_"*50)
##index method:this method return the index position of any character/word
str_c="learning python step by step"
print("index of p:", str_c.index('p'))       #index of p: 9
print("index of step:", str_c.index('step')) #index of step: 16

# print("index of w:",str_c.index("w"))
# ValueError: substring not found
print("_"*50)
## find method:- this method return the index position of exixting character or word, if target char is not avaliable then return -1
str_d="python programming"
print("check w is available:",str_d.find("w"))
# check w is available: -1

print("index of g:",str_d.find("g"))  #index of g: 10

##split method:this method split the string in list of character from target char/declimeter
str_e="india is best cricket team in the world"
world_list1=str_e.split(" ")
print(world_list1)
str_f="India#is#best#cricket#team#in#the#world"
print(str_f.split("#"))
['india', 'is', 'best', 'cricket', 'team', 'in', 'the', 'world']
['India', 'is', 'best', 'cricket', 'team', 'in', 'the', 'world']

url="https://www.facebook.com"
wl=url.split(".")
print(wl)    #['https://www', 'facebook', 'com']

w1=wl[0].split(":")[0]
print(w1)   #https

w2=wl[0].split("://")[1]
print(w2)    #https

w3=wl[1]
print(w3)   #facebook

w4=wl[2]
print(w4)  #com
print("_"*50)
##replace method: This method replace any world 1 with word2 in given string
str_j="python is easy to learn"
output=str_j.replace("python","java")
print(output)  #java is easy to learn

result2=str_j.replace("python","c+").replace("easy","hard")
print(result2)   #c+ is hard to learn

#Replace specific number of time the value
str_k="Python is easy to learn and python can solve any question, python community is very strong"
result_k=str_k.replace("python","java script",1)
print("result_k:",result_k)
#result_k: Python is easy to learn and java script can solve any question, python community is very strong

#Q1.write a python program to convert the all the lower case word in upper case
str1="USA is fighting With INDIA IN TRADE"
"""
1.get list of word using split method.
2.loop through each word from word list
3.if word.isupper then print(word.lower)
4.else word. islower then print(word.isupper)
"""
output=""
world_list1=str1.split(" ")

for word in world_list1:
    if word.isupper():
         output=output+word.lower()+" "
    elif word.islower():
         output=output+word.upper()+" "
    else:
        output=output+word+" "
print("output:",output)
# output: usa IS FIGHTING With india in trade
print("_"*50)
 ## strip method: this method removes all trailing spaces from given string
# trailing space: spaces as prefic or postfix
str_b= "   python programming   "
print(str_b)
#remove all trailing spaces
print(str_b.strip())

#lstrip and rstrip:these methods will removed left side and right side spaces
print(str_b.lstrip())  #removes left side spaces
print(str_b.rstrip()) #remove right side spaces

#remove all spaces in the given string
print(str_b.replace(" ", ""))
print("_"*50)

##Join method : this method helps us to join each character of string with any specific character or specail character
str_c="python"
result="_".join(str_c)
print("result:",result)   #result: p_y_t_h_o_n

#join each word of the list with space and create a string.
list1=['India','is','best','cricket','team','in','the','world']
result2=" ".join(list1)
print("result2:",result2)
# result2: India is best cricket team in the world

#check given string only contain numberss.
str_1="345664536"
str_2="546 6554"
print("str_1 is numeric:",str_1.isnumeric())   #str_1 is numeric: True
print("str_2  is numeric:",str_2.isnumeric())  #str_2  is numeric: False
print("_"*50)
##alnum method: this method check given string contain alphanumeric values.
str_3="python123"
str_4="programming 456"
print("str_3 is alpha numeric:",str_3.isalnum())  #str_3 is alpha numeric: True
print("str_4 is alpha numeric:",str_4.isalnum())  #str_4 is alpha numeric: False
print("_"*50)
#1. Write a python program to get all the emails and phone number given string.
user_details="""
On the tense 5654564545 final day 6754564598 of the 
Old  user3@yahoo.com Trafford user1@test.com Test, 
Shubman Gill lingered in the 90s 
for 36 deliveries.  user2@faceboo.com Since 2008,
there  user4@gmail.com have 8854564545 been 275 scores 
of 90 or more for """
world_list=user_details.split(" ")
for word in world_list:
    if word.isnumeric()and len(word)==10:
        print(word)
    if "@" in word and "gmail.com" in word:
        print(word)
"""
5654564545
6754564598
user4@gmail.com
8854564545
"""
#2.
str_d="hello We aRe learning PyThoN"
print(str_d.title())      #Hello We Are Learning Python
print(str_d.capitalize()) #Hello we are learning python
print(str_d.swapcase())   #HELLO wE ArE LEARNING pYtHOn

#3.write a python program to remove duplicate word from given string
str_k="Rahul mohit manjeet raghav rahul mohit manjeet"
result=" "
world_list=str_k.split(" ")
for word in world_list:
    if word not in result:
        result=result+word+" "
    else:
        continue
print("result string:",result)
# result string:  Rahul mohit manjeet raghav rahul

#4.write python program to get a longest word from given string
str_t="We are Learning Python Programming, Its Fun to learn"
max_len=0
long_word=" "
world_list=str_t.split(" ")
for word in world_list:
    word_len=len(word)
    if word_len>max_len:
        max_len=word_len
        long_word=word
        print(max_len,long_word)
    else:
        continue
print("longest word:",long_word)
# longest word: Programming,
















