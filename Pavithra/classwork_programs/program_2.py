units = int(input("Enter the number of units consumed :"))
if units < 100:
    print("total bill as per 15/unit rate :", units * 15)
elif units >= 100 and units <= 200:
    print("total bill as per 25/unit rate :", units *25)
elif units > 200:
    print("total bill as per 30/unit rate :", units * 30)
