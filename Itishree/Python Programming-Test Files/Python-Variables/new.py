a=34
print(a)
print("*"*50)
A = B = C = 200
print("Value of A:",A)
print("Value of B:",B)
print("Value of C:",C)
print("*"*50)
A,B,C=100,200,300
print("value of A",A)
print("value of B",B)
print("value of C",C)
############################
print("*"*50)
A,B,C=100,200,300
print(A,B,C) # 100 200 300
####################OPERATOR##############
#ADDITION OPERATOR#
print("*"*50)
var1 = 30
var2 = 20
print(var1+var2)  # 50
#########
print("*"*50)
print("Addition:",var1+var2) # Addition: 50
output=var1+var2
print(output)  #50
#SUBSTRACTION OPERATOR#
print("*"*50)
var1 = 60
var2 = 40
print(var1-var2)  #20
print("*"*50)
print("Substraction:",var1-var2)  # Substraction: 50
#MULTIPLICATION OPERATOR#
print("*"*50)
var1 = 70
var2 = 40
print(var1*var2)  # 2800
print("*"*50)
print("Multiplication:",var1*var2)  #Multiplication: 2800
#Division OPERATOR#
print("*"*50)
var1 = 50
var2 = 6
print(var1/var2)
print("Division /:",20/2)  # Division /: 10.0 -you can declare the number in print in division
print("*"*50)
print(var1//var2)   # 8 as double divison gives whole number
print("*"*50)
print("Remainder /:",var1/var2) #Remainder /: 8.333333333333334
print("Remainder /:",15%3)  # Remainder /: 0
##Compare Operators-==,!=#####
print("*"*50)
P = 400
Q = 400
R = 600
print(P==Q) # True
print(Q==R) #False
print(R==P) #False

###Get power of Value###
print("*"*50)
a=124
print("square of 124:",a**2) # square of 124: 15376-Here **2(square).
# you can increase number by using ** inorder to get more double of that value means a**5,here a =124;124*5 likewise
print("*"*50)
print("square of 12:",12**2) # square of 12 : 144-Here **2(Square)
print("cube of 7:",7**3) # cube of 7: 343 -Here **3(cube)

##To solve quadratic equation by using above operators##
#(a+b)^2=a^2+b^2+2ab
print("*"*50)
a = 10
b = 2
##can declare in muktiple way to compare between LHS AND RHS##
print((a+b)**2) #144
print("*"*50)
print("Square of a+b:",(a+b)**2) # Square of a+b: 144
print(a**2 + b**2 +2*a*b)
##Another way##
LHS=(a+b)**2
RHS= (a**2 + b**2 +2*a*b)
print(LHS==RHS) # True
print("*"*50)
a = 10
b = 2
c=((10+2)**2)
d=(10**2+2**2+2*10*2)
print (c==d)

#### Python Data Type####

####### Integer ############
var1 = 0
var2 = 156
var3 = 27777778889999
var4 = -3546
print(var1,type(var1)) # 0 <class 'int'>
print("-"*50)
print(var2,type(var2)) # 156 <class 'int'>
print("-"*50)
print(var3,type(var3)) # 27777778889999 <class 'int'>
print("-"*50)
print(var4,type(var4)) # -3546 <class 'int'>
print("-"*50)
####### Pointer ############
var1 = 0.5
var2 = 156.34
var3 = 27777778889999.124
var4 = -3546.23
print(var1,type(var1)) #0.5 <class 'float'>
print("-"*50)
print(var2,type(var2)) #156.34 <class 'float'>
print("-"*50)
print(var3,type(var3)) #27777778889999.125 <class 'float'>
print("-"*50)
print(var4,type(var4)) #-3546.23 <class 'float'>
print("-"*50)
####### Complex  ############
var1 = 5 + 28j # 5 as real number and 28j is imaginary number
print(var1,type(var1))
print("-"*50)
print("real number:", var1.real,type(var1))      #real number: 5.0 <class 'complex'>
print(" imaginary number:", var1.imag,type(var1)) #imaginary number: 28.0 <class 'complex'>
print("-"*50)
# in other way####
var1 = 7 + 125j
print(var1,type(var1))
print("-"*50)
print(var1.real,type(var1)) #7.0 <class 'complex'>
print(var1.imag,type(var1)) #125.0 <class 'complex'>
print("-"*50)
#################
P2 = -90 - 1259j
print(P2,type(P2))
print("-"*50)
print(P2.real,type(P2)) # -90.0 <class 'complex'>
print (P2.imag,type(P2)) #-1259.0 <class 'complex'>
########String################
print("-"*50)
str1 = ''
print(str1,type(str1))  #<class 'str'>
print("-"*50)
S2 = "Hey"
print(S2,type(S2)) # Hey <class 'str'>
print("-"*50)
S3 = """
40 fghhbbbbbbbjbjbjbbbhbhbhbhbhjbhjbhjbhjbhjbhbhbhjbhjbhbhjbhjbhbhjbhjbhbhjbbbbbbbbbbbbbbbbbbbbbbbbbb
hjbjbnbn nnbb """
print(S3,type(S3)) #
S1="Itishree"
print (S1[1])  #t +ve indexing
print (S1[-1]) #e -ve indexing
print("-"*50)
S2 = 'Mani'
print (S2[0],type(S2)) # M +ve indexing <class 'str'>
print (S2[-4],type(S2))# M -ve indexing <class 'str'>
###########List################
l1 =[4,5,-6,7]
print(l1[2]) # -6 +ve indexing
print(l1[-3],type(l1)) # 5 -ve indexing
print("-"*50)
print(l1[2],l1[-3],type(l1)) #-6 5
list1 = [2,0.5,"Hello",]
print (list1,type(list1)) # [2, 0.5, 'Hello'] <class 'list'>
print("-"*50)
l1 = [2,5.9,4+7j,"Hello",[1,7,8],(31,7,8),{1:123},{5,7,8}]
print (l1,type(l1)) # [2, 5.9, (4+7j), 'Hello', [1, 7, 8], (31, 7, 8), {1: 123}, {8, 5, 7}] <class 'list'>
print("-"*50)
list2 = [23,78,99]
list2.append(100)
print(list2,type(list2)) # [23, 78, 99, 100] <class 'list'>-Here we have added 100 wkth help of append method
                         # as a new number to the existing list numbers.
                         # so we have upddte/modify the data.hence it is mutuable
print("-"*50)
l3=[76,87,90,55,200]
l3.append(2000)
print(l3,type(l3)) # [76, 87, 90, 55, 200, 2000] <class 'list'>
###########Tupule################
tup1 =(98,77,200)
print (tup1,type(tup1)) # (98, 77, 200) <class 'tuple'>
tup2 = (5,5.6,"Rema",[3,4.5,7],(1,5,7),{'name:tom'},True,False,None) #(5, 5.6, 'Rema', [3, 4.5, 7], (1, 5, 7), {'name:tom'}, True, False, None) <class 'tuple'>
print(tup2,type(tup2))
print(tup2[2], type(tup2[2]))
print("-"*50)
print(tup2[0],type(tup2))  # 5 <class 'tuple'>
print("-"*50)
print(tup2[-8],type(tup2)) # 5.6 <class 'tuple'>
print("-"*50)
tup2 = (5,5.6,"Rema",[3,4.5,7],(1,5,7),{'name:tom'},True,False,None) #(5, 5.6, 'Rema', [3, 4.5, 7], (1, 5, 7), {'name:tom'}, True, False, None) <class 'tuple'>
print(tup2,type(tup2))
print(tup2[2], type(tup2[2])) # Rema <class 'str'>
print(tup2[5], type(tup2[5]),type(tup2)) # {'name:tom'} <class 'set'> <class 'tuple'>
#########Dictionary Data Type #####################
print("-"*50)
dict1 = {'a':2,'name':'mani','age':32,'address':'BLR','email':'iti.rema@gmail.com'}
print(dict1,type(dict1))
#{'a': 2, 'name': 'mani', 'age': 32, 'address': 'BLR', 'email': 'iti.rema@gmail.com'} <class 'dict'>

dict1 = {'a':2,'name':'mani','age':32,'address':'BLR','email':'iti.rema@gmail.com'}

print("NAME:",dict1['name']) #NAME: mani
print("AGE:",dict1['age']) #AGE: 32

print("-"*50)
dict1 = {'a':2,'name':'mani','age':32}
print(dict1['a'],['name'],type(dict1)) #2 ['name'] <class 'dict'>

print("-"*50)

dict1['Country'] = "India"
dict1['Pincode'] = 560037
print(dict1) # {'a': 2, 'name': 'mani', 'age': 32, 'Country': 'India', 'Pincode': 560037}
print("-"*50)
dict2 = {'a':2,'name':'mani','age':32,'address':'BLR','email':'iti.rema@gmail.com'}
dict2['Country','Pincode'] = "India",560037
print(dict2)
#{'a': 2, 'name': 'mani', 'age': 32, 'address': 'BLR', 'email': 'iti.rema@gmail.com', ('Country', 'Pincode'): ('India', 560037)}
#QUESTION TO ASK-how to enter multiple record at once
print("-"*50)
dict1 = {'a':2,'name':'mani','age':32,'age':34}
print(dict1) # {'a': 2, 'name': 'mani', 'age': 34}->No duplicate values .as there are two age key value is here,
 # it choose in LIFO manner s
######################SET#############
set1={1,4,5,6,4,3,7,8,9,7}
print(set1,type(set1)) # {1, 3, 4, 5, 6, 7, 8, 9} <class 'set'>
set1.add(100)
print(set1,type(set1))#{1, 3, 4, 5, 6, 7, 8, 9, 100} <class 'set'>

# New value added as 100 in existing set list.so it is mutuable.We have use 'ADD' method for set to add new value
#QUESTION TO ASK-why append cant use for set data type to add new value
#Same for list why add cant be used to add new value









