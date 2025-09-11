# write a python program to get total as per the purchase

print("_"*50)
fruit_inventory = {'Apple': 100, 'Banana': 150, 'Mango': 200, 'watermelon': 300}
fruit_with_price = {'Apple': 50, 'Banana': 10, 'Mango': 60, 'watermelon': 35}
fruit_purchased = {'Apple': 10, 'Banana': 20, 'Mango': 15, 'watermelon': 5}

print(fruit_purchased['Apple'])

total_bill = 0
# fruit_inventory[fruit_name] = fruit_inventory[fruit_name] - fruit_purchased[fruit_name]
for k, v in fruit_with_price.items():
    # Get fruit
    fruit_name = k
    fruit_price = v
    fruit_no =  fruit_purchased[fruit_name]
    fruit_bill = fruit_no * fruit_price
    total_bill = total_bill + fruit_bill
    fruit_inventory[fruit_name] = fruit_inventory[fruit_name] - fruit_purchased[fruit_name]
    print(fruit_name, "|", fruit_price, "|", fruit_no, "|", fruit_bill)

print("_"*20)
print("total bill :", total_bill)
print(fruit_inventory)


