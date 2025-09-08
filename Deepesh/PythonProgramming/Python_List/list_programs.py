# write a python program to get of sum of all values:
list1 = [4, 6, 8, 2, 5, 8]
sum_values = 0
for val in list1:
    sum_values = sum_values + val


print("sum of values :", sum_values)
# sum of values : 33

print("_"*50)
#########################
# write a python program to get max value from list
list1 = [5, 7, 2, 56, 108, 3, 88]
max_val = 0
for abc in list1:
    if abc > max_val:
        max_val = abc
    else:
        continue

print("max value of list :", max_val)
# max value of list : 108


print("_"*50)
#########################
# write a python to get second max number from list.
list2 = [5, 97, 2, 560, 10, 301, 88]
max_val = 0
sec_max = 0
for val in list2: # 5, 97, 2, 560, 10, 301, 88
    if val > max_val: # 5, 97, 560
        max_val = val # 5, 97, 560
    elif sec_max < val < max_val: # 2, 10, 301
        sec_max = val # 2, 10, 301


print("sec max value :", sec_max)

