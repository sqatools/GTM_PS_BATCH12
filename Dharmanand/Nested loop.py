##Nested for loop : In the nested loop for each single value of outer loop, entire inner value will be executed.

for i in range(1, 5):
    print("Address :i:",i)
    for j in range(1, 3):
        print("Package :j:", j)

print("#"*50)

##=======================

#break and continue statement:
#continue statement: if any condition is met with continue statement, then it will not execute remaining code but it will move to next iteration of for loop.

for i in range(1,5):
    if i in [2, 4]:
        continue
    print(i)


print("#"*50)
##break statement - will break the execution of for loop if the condition is matching
for i in range(1,5):
    if i in [2,3]:
        break
    print(i)

print("#"*50)

for i in range(1,5):
    if i ==3:
        break

    print (i)

print ("#"*50)



for num in range (3,100):
    prime = True
    for j in range(3, num):
        if num%j == 0:
            prime = False
            break
            if prime:
                print(num)









