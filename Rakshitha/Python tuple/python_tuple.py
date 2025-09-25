tup1=(5,7,8,12,4,7,25,'hello',[3,5,7],(3,2,1))
print(tup1,type(tup1))
# (5, 7, 8, 12, 4, 7, 25, 'hello', [3, 5, 7], (3, 2, 1)) <class 'tuple'>

print(tup1[3])        #12
print(tup1[-2])       #[3, 5, 7]
print(tup1[-3:-8:-1]) #('hello', 25, 7, 4, 12)
print(tup1[:3:1]*2)   #(5, 7, 8, 5, 7, 8)
print(tup1[-2][-1]**2)#49
print("_"*50)

print(dir(tuple))
['count', 'index']

tup2=(4,6,'a','b','a','c',7,8)
print("count of a:",tup2.count('a'))   #count of a: 2
print("index of c:",tup2.index('c'))   #index of c: 5

print("count of :", tup2.count('b')) #count of : 1
print("index of c :", tup2.index(7)) # index of c : 6
print("_"*50)
############## tuple comprehension #######
tup3=(4,7,9,12,56,17,8)
result=(val for val in tup3 if val%2!=0)
print("odd values:",tuple (result))  #odd values: (7, 9, 17)

### get square of all the values
tup4=(4,7,9,12,5,17)
result3=((val,val**2)for val in tup3)
print("result3:",tuple(result3))
# result3: ((4, 16), (7, 49), (9, 81), (12, 144), (56, 3136), (17, 289), (8, 64))

