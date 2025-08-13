
# Q1. Python program to show exam result as per marks received.

marks = int(input("Enter your marks: "))

if marks > 100:
    print("Invalid marks, cannot be more than 100.")
elif marks > 25:
    print("passed with grace marks")
elif marks < 30:
    print("Failed in exam.")
elif marks > 80:
    print("Passed with Excellent Performance division.")
elif marks > 60:
    print("Passed with 1st division.")
elif marks > 50:
    print("Passed with 2nd division.")
elif marks > 30:
    print("Passed with 3rd division.")
