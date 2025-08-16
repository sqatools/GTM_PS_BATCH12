marks = int(input("Enter your marks: "))

if marks > 35 and marks < 50:
    print("You are passed in 3rd class")

elif marks > 50 and marks < 70:
    print("You are passed in 2nd class")

elif marks > 70 and marks <= 100:
    print("You are passed in 1st class")

else:
    print("Status: You have failed in the exam")