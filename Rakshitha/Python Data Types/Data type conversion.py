############## Integer ###########
## Int-float ##
n1=60
f1=float(n1)
print(f1,type(f1)) #60.0 <class 'float'>

## Int-string ##
n2=789
s2=str(n2)
print(s2,type(s2)) #789 <class 'str'>
"""
## Int-list ## conversion is not possible
n3=74125
l1=list(n3)
print(l1, type(l1)) #TypeError: 'int' object is not iterable
"""
## int-list ## conversion is not possible
## int-tuple ## conversion is not possible
## int-dict ## conversion is not possible
## int-set ## conversion is not possible

## Int-boolean ##
a1=0
b1=bool(a1)
print(b1, type(b1)) #False <class 'bool'>

a2=10
b2=bool(a2)
print(b2, type(b2)) #True <class 'bool'>
print("_"*50)

############## Float ################
## float-int
f1=67.77
n1=int(f1)
print(n1,type(n1)) #67 <class 'int'>

## float-string
f2=87.45
s2=str(f2)
print(s2,type(s2)) #87.45 <class 'str'>
print(s2,type(s2),s2[3]) #87.45 <class 'str'> 4

## float-list ## conversion is not possible
## float-tuple ## conversion is not possible
## float-dict ## conversion is not possible
## float-set ## conversion is not possible

##float-boolean
f1=0.0
b1=bool(f1)
print(b1,type(b1)) #False <class 'bool'>

f2=71.55
b2=bool(f2)
print(b2,type(b2)) #True <class 'bool'>
print("_"*50)

############# String ###########
## str-int
s1='57883'
n1=int(s1)
print(n1,type(n1)) #57883 <class 'int'>

s1='4558'
print(s1, type(s1),s1[0]) #4558 <class 'str'> 4

## string-float
s2="82.65"
f2=float(s2)
print(f2, type(f2)) #82.65 <class 'float'>

## string-list/tuple
str3="python"
l3=list(str3)
print(l3,type(l3)) #['p', 'y', 't', 'h', 'o', 'n'] <class 'list'>

str3="python"
t3=tuple(str3)
print(t3,type(t3)) #('p', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

## String-set
s5="programming"
set3=set(s5)
print(set3,type(set3)) #{'a', 'm', 'p', 'n', 'g', 'i', 'o', 'r'} <class 'set'>

## string-dict ## conversion is not possible
## string-boolean behvaes like int
# if string is empty then coversion is false
# if string contain some value, then conversion is true.
print("_"*50)
################### list #################
## list-int ## conversion is not possible
## list-float ## conversion is not possible
## list-string ## not important
l1=[7,5,9]
str1=str(l1)
print(str1,type(str1),str1[0],str1[1]) #[7, 5, 9] <class 'str'> [ 7

## list-tuple/set
l2=[7,4,1,3]
t2=tuple(l2)
print(t2, type(t2)) #(7, 4, 1, 3) <class 'tuple'>

s2=set(l2)
print(s2,type(s2)) #{1, 3, 4, 7} <class 'set'>
## list-dict ## converion is not possible
## list-boolean ## same as int, string
print("_"*50)
############# Tuple ##################
## Tuple- int ## converion is not possible
## tuple-float ## converion is not possible
## tuple-string # not important

## tuple-list
t1=(1,7,8,9)
l1=list(t1)
print(l1,type(l1)) #[1, 7, 8, 9] <class 'list'>

## tuple-dict ## conversion is not possible

## tuple-set
t2=(8,52,87,7)
s2=set(t2)
print(s2,type(s2)) #{8, 52, 7, 87} <class 'set'>
print("_"*50)

################ Dictionary ###################
# dict-int ## conversion is not possible
# dict-float ## conversion is not possible
# dict-string ## not important
# dict-list/tuple/set ## conversion is not possible
dict1={'a':123,'b':2333,'c':963}
l1=list(dict1)
print(l1, type(l1)) #['a', 'b', 'c'] <class 'list'>

t1=tuple(dict1)
print(t1,type(t1)) #('a', 'b', 'c') <class 'tuple'>

s1=set(dict1)
print(s1,type(s1)) #{'a', 'b', 'c'} <class 'set'>
print("_"*50)
############### set #################
# set->int ## conversion is not possible
# set-float ## conversion is not possible
# set-string ## conversion is not possible
# set-dict ## conversion is not possible
## set-list/tuple ## conversion is not possible
s1=[78,4,58,6]
l1=list(s1)
print(l1,type(l1)) #[78, 4, 58, 6] <class 'list'>

t1=tuple(s1)
print(t1,type(t1)) #(78, 4, 58, 6) <class 'tuple'>


















