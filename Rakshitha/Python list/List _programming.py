#Q1.write a python program to get of sum of all values:
list1=[4,8,5,7,12]
sum_values=0
for val in list1:
    sum_values=sum_values+val
print("sum of values:",sum_values)
#sum of values: 36

#Q2.write a python program to get max value from list:
list1=[5,7,2,56,108,3,88]
max_val=0
for val in list1:
    if val> max_val:
        max_val=val
    else:
        continue
print("max_val:",max_val)
# max_val: 108

#Q3.write a python program to get sec max number from list:
list2=[5,97,2,560,10,301,88]
max_val=0
sec_val=0
for val in list2:
    if val>max_val:
        max_val=val
    elif sec_val<val<max_val:
        sec_val=val
print("sec_max value:",sec_val)
# sec_max value: 301
