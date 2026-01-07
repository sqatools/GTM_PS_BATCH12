# write a python program to get total as per the purchase

print("_"*50)
# fruit_inventory = {'Apple': 100, 'Banana': 150, 'Mango': 200, 'watermelon': 300}
fruit_with_price = {'Apple': 50, 'Banana': 10, 'Mango': 60, 'watermelon': 35}
fruit_purchased = {'Apple': 10, 'Banana': 20, 'Mango': 15, 'watermelon': 5}

print(fruit_purchased['Apple'])

total_bill = 0
for fruit,price in fruit_with_price.items():


    fruit_name = fruit
    fruit_price = price
    fruit_no = fruit_purchased[fruit_name]
    fruit_bill = fruit_no * fruit_price
    total_bill = total_bill + fruit_bill
    print(fruit_name, "|",fruit_price, "|",fruit_no, "|",fruit_bill)
print("_"*20)
print("total bill:",total_bill)
"""
10
Apple | 50 | 10 | 500
Banana | 10 | 20 | 200
Mango | 60 | 15 | 900
watermelon | 35 | 5 | 175
____________________
total bill: 1775
"""
print("_"*50)
fruit_inventory = {'Apple': 100, 'Banana': 150, 'Mango': 200, 'watermelon': 300}
fruit_with_price = {'Apple': 50, 'Banana': 10, 'Mango': 60, 'watermelon': 35}
fruit_purchased = {'Apple': 10, 'Banana': 20, 'Mango': 15, 'watermelon': 5}

print(fruit_purchased['Apple'])

total_bill = 0
for fruit,price in fruit_with_price.items():
    fruit_name = fruit
    fruit_price = price
    fruit_no = fruit_purchased[fruit_name]
    fruit_bill = fruit_no * fruit_price
    total_bill = total_bill + fruit_bill
    fruit_inventory[fruit_name] = fruit_inventory[fruit_name] - fruit_purchased[fruit_name]
    print(fruit_name, "|",fruit_price, "|",fruit_no, "|",fruit_bill)
print("_"*20)
print("total bill:",total_bill)
print(fruit_inventory)
# total bill: 1775
# {'Apple': 90, 'Banana': 130, 'Mango': 185, 'watermelon': 295}