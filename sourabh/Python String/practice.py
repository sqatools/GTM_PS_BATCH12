age = [12, 15, 18, 23, 5, 30, 35]
output = []

for val in age:
    if val >= 18:
        print("Eligible for voting:", val)
        output.append(val)
    else:
        print("User not eligible:", val)

print("All eligible ages:", output)
##########################################################
print("_"*50)

list1 = ['a', 'b', 'c', 'd']
list2 = [12, 13, 24, 15]
output = []
for i in range(len(list1)):
    output.append((list1[i], list2[i]))
print(output)