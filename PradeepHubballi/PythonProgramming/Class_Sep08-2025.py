user_age =[12,15,18,23,5,30,35]

age =[u_age for u_age in user_age if u_age >=18]
print("Output:",age)

# write a python program to great a list combination from 2 lists
list1 = ['a', 'b', 'c', 'd']
list2 = [12, 13, 24, 15]

#output = [('a', 12), ('b', 13), ('c', 24), ('d', 15)]

combi = []
list_len =len(list1)
for i in range(list_len):
    print(i,list1[i],list2[i])
    combi.append((list1[i],list2[i]))
print(combi)
##[('a', 12), ('b', 13), ('c', 24), ('d', 15)]