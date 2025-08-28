####################Integer################################
########Int - > Float###########
n1 = 50
f1 =float(n1)
print(f1, type(f1))

########Int - >String###########
int1 = 785
s1= str(int1)
print(s1, type(s1))

##########Int -> List###Conversion not possible
"""
n3 = 325436
list1 = list(n3)
print(list1, type(list1))

Int -> Tuple Conversion not possible
Int ->Dictionary Conversion not possible
Int -> Set Conversion not possible
"""
# Int = Boolean

int7 = 84
b1 = bool(int7)
print(b1, type(b1))

int8 = 0
b2 = bool(int8)
print(int8, type(int8))

###########################Float##################################
print("_"*99)
#########Float -> Int####
f1 = 85.84
i1 = int(f1)
print(i1, type(i1))
#############Float - String########
f2 = 84.84
str1 = str(f2)
print(str1, type(str1))
print(str1[2])

#Float - List not possible
#Float - Tuple not possible
#Float - Set not possible
#Float - Dictionary not possible

#####Float -> Boolean

fl1 = 69.84
b4 = bool(fl1)
print(b4, type(b4))

fl2 = 0.00
b5 = bool(fl2)
print(b5, type(b5))

##############String##############
#String ->Integer
# If string contains only words/ char , then conversion is not possible
#If string contains only numbers then conversion is possible.

s1 = "8407"
print(s1, type(s1))
n1 = int(s1)
print(n1, type(n1))

#String -> Float
s2 ="8584"
flt1 = float(s2)
print(flt1, type(flt1))

# String -> List
print("_"*100)
str3 = "Expert"
lst1 = list(str3)
print(lst1, type(lst1))

# String -> Tuple
print(("**"*50))
str4 = "Abhijeet"
tup1 = tuple(str4)
print(tup1, type(tup1))

print("****"*50)
#String -> Dictionary conversion is not possible

#String -> Set conversion
s5 = "Programming"
set1 = set(s5)
print(set1, type(set1))

# String ->Boolean - behaves like int
# if string empty then conversion is false
# If string contains some value, then conversion is True
#############################List###################################

# List -> int not possible
# List - > float is not possible
# list -> String not important

#List -> Tuple
l2 = [1, 2 ,7, 9]
tup2 = tuple(l2)
print(tup2, type(tup2))

####List ->Dictionary Not possible

# List -> Set
l3 = [ 5, 7, 8, 9, 3]
s1 = set(l3)
print(s1, type(s1))

# List -> boolean same as int , string

#######################Tuple######################
#Tuple -> Int conversion not possible
#Tuple -> float conversion not possible
#Tuple -> string conversion not possible
#Tuple -> list
t1 = ( 1, 3, 7, 9)
ls1 = list(t1)
print(ls1, type(ls1))

#Tuple ->Dictionary not possible
# Tuple ->set
t3 = (5, 7, 19, 20 , 21)
s3 = set(t3)
print(s3, type(s3))

#Tuple to int not possible
t2 = (4, 5)
n1 = int(t2)