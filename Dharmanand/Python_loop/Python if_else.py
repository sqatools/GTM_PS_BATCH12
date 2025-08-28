# Get number of units from user
units = int(input("Enter the number of units consumed: "))

# Calculate bill
if units > 200:
    rate = 30
elif units > 100:   # Covers 101–200
    rate = 25
else:               # Covers 0–100
    rate = 15

bill = units * rate

# Display result
print(f"Units Consumed: {units}")
print(f"Rate per Unit: ₹{rate}")
print(f"Total Bill: ₹{bill}")