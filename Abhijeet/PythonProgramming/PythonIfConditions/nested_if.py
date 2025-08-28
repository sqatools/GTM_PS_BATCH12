from xml.dom.minidom import ProcessingInstruction

round1 = "Pass"
round2 = "Pass1"
round3 = "Pass1"

if round1 =="Pass":
    print("Congrats, 1st round is cleared")
    if round2 =="Pass":
        print("Congrats, 2nd round is cleared")
        if round3 =="Pass":
            print("Congrats, 3rd round is cleared")
        else:
            print('Not selected in third round')
    else:
        print("Second round is not clear")

else:
    print("First round is not clear")

##################################################
# Single line of if condition checking
var = 84
output = "even" if var%2 ==0 else "odd"

print("output:", output)

# Python code to check given value is available in the list
v1 = 13
list1 = [3, 5, 7, 2, 45 , 27]
output2 = True if v1 in list1 else False
print("Output2:", output2)

if 13  in list1:
    print("v1 is available in list1")
else:
    print("v1 is not available in list1"
          )
#############
#Python code to check given value is available in the list
v1 = 12
v2 = 50

list1 = [3, 5 , 7 , 2, 23, 12]
result = True if v1 in list1 else False
print("output2:", result)
print(True if v1 in list1 else False)

if v1 in list1:
    print(f"v1: {v1} is available in {list1}")
else:
    print(f"{v1}is not available in  {list1}")

# Check v2 is not available in the list1

if v2 not in list1:
    print(f"v2: {v2} is not available in list1: {list1}")
else:
    print(f"v2: {v2} is available in list1 : {list1}")

###############################################33333
print("_"*184)
# is, is not operator
# is compare 2 objects
list1 = [6, 8 , 23, 45, 12]
list2 = [6, 8 , 23, 45, 12]
list3 = list1

if list1 is list2:
    print("Both list objects are same")
else:
    print("Both list objects are not same")

if list1 == list2:
    print("Both list have same values")

else:
    print("Both list have diff values")




##################Python code to check given value is available in the list

v1 = 12
v2 = 50

list1 = [3, 5, 7, 2, 45, 23, 12]
result = True if v1 in list1 else False
print("output2 :", result)
print(True if v1 in list1 else False)
