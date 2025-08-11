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