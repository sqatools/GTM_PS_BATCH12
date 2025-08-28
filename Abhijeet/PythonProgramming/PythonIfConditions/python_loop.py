list1 = [5, 6, 8, 2, 4, "Hello", 3.2, [5,6,7], True]

#Get each value from list
for a in list1:
    print(a, type(a))


#########Use range function in loop##########
"""
range(start, end, step) function
-> Range output include start and exclude the end value
-> Default start value is zero, if do not enter any value
-> Default step value is 1 if you do not enter any value


"""
for i in range(1, 10, 2):
    print(i)


print("_"*100)
#Keep start value and default value as default
for k in range(15):
    print(k)

print("**"*50)
# Write a program to add all value from 1 to 10

add = 0
for val in range(1, 11, 1):
    add = add + val
print("Sum of 1 to 10 :",add)