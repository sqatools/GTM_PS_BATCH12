from pprint import pprint
"""
# Properties:
->  dict is mutable datatype, that we can modify any point of time.
->  dict store data in key:value format with curly braces e.g  {'a': 123}
->   dict only contains uniques keys, duplicate keys are not allowed.
    if we define any duplicate key, then it consider the latest define value
->  Only immutable data type can be key in the dict. e.g int, float, complex, string, tuple, boolean.
->  There is no restriction of value data in the dict. all type of data can be value in dict.
->  Dict store data in LIFO ( LAST IN FIRST OUT ) format.
->  Dict does not follow indexing.
"""

dict2={'a':123,'b':345}
print(dict2,type(dict2))
# {'a': 123, 'b': 345} <class 'dict'>

# get values from dict
print(dict2['a'])   #123

#add values to dict
dict2['c']=457
print("dict2:",dict2)
#dict2: {'a': 123, 'b': 345, 'c': 457}

dict2['d']=[4,7,9,2]
print("dict2:",dict2)
# dict2: {'a': 123, 'b': 345, 'c': 457, 'd': [4, 7, 9, 2]}
#Adde value in the list of dict
dict2['d'].append(100)
print("dict2:",dict2)
# dict2 : {'a': 123, 'b': 345, 'c': 457, 'd': [4, 7, 9, 2, 100]}

val=dict2['d'].pop(1)
print("remove values:",val)
print("dict2:",dict2)
# remove values: 7
# dict2: {'a': 123, 'b': 345, 'c': 457, 'd': [4, 9, 2, 100]}

#add list as kye in the dict :list can not be key in the dictionary
# dict2[[1,5,9]]=[4,7,90]
# print("dict2:",dict2)  #TypeError: unhashable type: 'list'

### multiple level of dictionary
dict3={123 :[5,6,8],5.6:(4,7,9),
       'python':123,(3,7,8):
           {'a': 33, 'b': 67}
       }
print(dict3)
# {123 : [5, 6, 8], 5.6: (4, 7, 9), 'python': 123, (3, 7, 8): {'a': 33, 'b': 67}}
print("_"*50)

#Replace 8 with 18 in [5,6,8] from 123 key.
dict3={123:[5,6,8],5.6:(4,7,9),'python':123,(3,7,8):{'a':33,'b':67}}
print(dict3[123]) #[5, 6, 8]
dict3[123][2] = 18
print(dict3[123]) #[5, 6, 18]
print("_"*50)

# how to apply loop on dictionary
dict4={'p':22, 'q':33, 'r':44, 's':55, 't':66}
#in this loop user will get only keys.
for val in dict4:
    print(val,end=" ")
# p q r s t
print("_"*50)

#Get key and value from loop
for val in dict4.items():
    print(val,end=" ")
# ('p', 22) ('q', 33) ('r', 44) ('s', 55) ('t', 66)

for k,v in dict4.items():
    print(k,":",v)
"""
q : 33
r : 44
s : 55
t : 66
"""
print("_"*50)
## writer a python program to get square of each value return as dict
dict_a={'a':4, 'b':5,'c':6}
output={}
for k1,v1,in dict_a.items():
    output[k1]=v1**2
    print(k1,":",v1**2)
print(output)
""""""
a : 16
b : 25
c : 36
{'a': 16, 'b': 25, 'c': 36}
""""""
print("_"*50)

# write a python to get sqaure of each even values and return as dict
dict_a={'w':7,'x':4,'y':5,'z':6}
result2={}
for k2,v2 in dict_a.items():
    if v2%2==0:
        result2[k2]=v2**2
        print(k2,":",v2)
    else:
        continue
print("output:",result2)
# output: {'x': 16, 'z': 36}
print("_"*50)

############## methods in dictionary ############

print(dir(dict))
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
print("_"*50)
#Add data to the list
#update method:- The method update one dict data to another dict
d1={'w':7,'x':4,'y':5,'z':6}
d2={'p':123,'q':456}

d1.update(d2)
print("d1:",d1)  #d1: {'w': 7, 'x': 4, 'y': 5, 'z': 6, 'p': 123, 'q': 456}
print("d2:",d2)  # d2: {'p': 123, 'q': 456}

print("_"*50)
#item() method: This method return the list of key value pair as tuple in the list
result=d1.items()
print("item result:",result)
#item result: dict_items([('w', 7), ('x', 4), ('y', 5), ('z', 6), ('p', 123), ('q', 456)])

print("_"*50)
# get method: this method return value of any specific key in the dictionary
d3={'w':7,'x':4,'y':5,'z':6,'p':12,'Q':456}
print(d3.get('Q')) #456

print("_"*50)
# key() and values()methods
print("list of keys:",d3.keys())   #(['w', 'x', 'y', 'z', 'p', 'Q'])
print("list of values:",d3.values()) #([7, 4, 5, 6, 12, 456])

print("_"*50)
# pop method:this method removes data from dictionary with the help of keys
d4={'w':7,'x':4,'y':5,'z':6,'p':12,'Q':456}
val=d4.pop('Q')
print("remove value:",val)
print("d4:",d4)
# remove value: 456
# d4: {'w': 7, 'x': 4, 'y': 5, 'z': 6, 'p': 12}

print("_"*50)
# pop items()method: this method will remove key value pair from dictionary and returnas tuple
d5={'w': 7, 'z': 6, 'P': 123, 'Q': 456, 'X': 788, 'Y': 345}
val=d5.popitem()
print("removed val:",val)  #removed val: ('Y', 345)
print("d5:",d5)            #d5: {'w': 7, 'z': 6, 'P': 123, 'Q': 456, 'X': 788}

print("_"*50)
# clear method: this method clear all the data from dictionary only empty dictionary will be removed
d6={'w': 7, 'z': 6, 'P': 123, 'Q': 456, 'X': 788, 'Y': 345}
d6.clear()
print("dict6:",d6)  #dict6: {}

print("_"*50)
# copy()method: copy method help us to copy one dict data to another dict.
# shallow copy :- In case of shallow copy if modify any dict, then changes will reflect in both dictionaries
d7={'w': 7, 'z': 6, 'P': 123, 'Q': 456, 'X': 788, 'Y': 345}
d8=d7
d8['Z']=100
d7['R']=200
print("d7:",d7)
print("d8:",d8)
# d7: {'w': 7, 'z': 6, 'P': 123, 'Q': 456, 'X': 788, 'Y': 345, 'Z': 100, 'R': 200}
# d8: {'w': 7, 'z': 6, 'P': 123, 'Q': 456, 'X': 788, 'Y': 345, 'Z': 100, 'R': 200}

print("_"*50)
# deep copy:- In deep copy concept if we will modify any of the dict, then changes will reflect in respective dict only
A1={'a':333,'b':444}
B1=A1.copy()
B1['c']=500
A1['d']=666
print("A1:",A1)  #A1: {'a': 333, 'b': 444, 'd': 666}
print("B1:",B1)  #B1: {'a': 333, 'b': 444, 'c': 500}

print("_"*50)
# write a python program to move values from one dict to another dict
h1 = {'A': 567, 'B': 678, 'C': 234}
h2 = {}
temp=h1.copy()
for k in temp:
    print(k)
    val=h1.pop(k)  #remove data from dict with hepl of key
    h2[k]=val #assing removed data to new dict

print("h2:",h2)
print("h1:",h1)
"""
A
B
C
h2 : {'A': 567, 'B': 678, 'C': 234}
h1 : {}
"""


print("_"*50)
###############################################
# write a python program to create a dictionary from given string
str1= "Very good Morning Learning Python"
#ouptut = {"V": "Very", "g": "good", "M": "Morning", "L": "Learning", "P": "Python"}
output={}
word_list=str1.split(" ")
print(word_list)
for word in word_list:
    print(word,":",word[0])
    first_char=word[0]
    output[first_char]=word
print("output:",output) #output: {'V': 'Very', 'g': 'good', 'M': 'Morning', 'L': 'Learning', 'P': 'Python'}

"""
['Very', 'good', 'Morning', 'Learning', 'Python']
Very : V
good : g
Morning : M
Learning : L
Python : P
output: {'V': 'Very', 'g': 'good', 'M': 'Morning', 'L': 'Learning', 'P': 'Python'}
"""
print("_"*50)
###############################################
# write a python program to create a dictionary from given string
str1= "Very good Morning Learning Python"
#ouptut = {"Vy": "Very", "gd": "good", "Mg": "Morning", "Lg": "Learning", "Pn": "Python"}
output={}
word_list=str1.split(" ")
print(word_list)
for word in word_list:
    print(word,":",word[0])
    first_char=word[0]
    last_char= word[-1]
    output[f"{first_char}{last_char}"]=word[0]

print("output:",output)  #output: {'Vy': 'V', 'gd': 'g', 'Mg': 'M', 'Lg': 'L', 'Pn': 'P'}

print("_"*50)
# sort dict data sorted function
test_dict={'a':5,'c':2,'b':10}
sorted_result=dict(sorted(test_dict.items()))
print("sorted result:",sorted_result)
# sorted result: {'a': 5, 'b': 10, 'c': 2}
