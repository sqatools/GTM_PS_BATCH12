# Q1.find out all the eligible condition to vote whose age>=18
users_age=[12,15,1,23,5,30,35]
for age in users_age:
    if age >=18:
        print("user is eligible for voting:",age)
    else:
        print("user is not eligiable ")
"""
user is not eligiable 
user is not eligiable 
user is not eligiable 
user is eligible for voting: 23
user is not eligiable 
user is eligible for voting: 30
user is eligible for voting: 35
"""
print("_"*50)
users_age=[12,15,18,23,5,30,35]
output=[]
for age in users_age:
    if age >=18:
        print("user is eligible for voting:",age)
        output.append(age)
    else:
        print("user is not eligiable ")

print("output:",output)
"""
user is not eligiable 
user is not eligiable 
user is eligible for voting: 18
user is eligible for voting: 23
user is not eligiable 
user is eligible for voting: 30
user is eligible for voting: 35
output: [18, 23, 30, 35]
"""

# Q2.write a python program to creat a list combination from 2 lists
list1=['a','b','c','d']
list2=[12,13,24,15]

combi=[]
list_len=len(list1)
for i in range(list_len):
    print(i,list1[i],list2[i])
    combi.append((list1[i],list2[i]))
print(combi)
"""
0 a 12
1 b 13
2 c 24
3 d 15
[('a', 12), ('b', 13), ('c', 24), ('d', 15)]
"""
# output=[(list1[i],list2[i] for i in range(len(list1)))]