fruit_inventory = {'Apple':100,'Banana' :15,'Mango':200,'Watermelon':300}
fruit_with_price = {'Apple':50,'Banana' :10,'Mango':60,'Watermelon':35}
fruit_purchased = {'Apple':10,'Banana' :20,'Mango':15,'Watermelon':5}

print(fruit_purchased['Apple'])

total_bill =0

for k,v, in fruit_with_price.items():
    fruit_name=k
    fruit_price=v
    fruit_no = fruit_purchased[fruit_name]
    fruit_bill = fruit_no * fruit_price
    total_bill = total_bill + fruit_bill
    fruit_inventory[fruit_name] = fruit_inventory[fruit_name] - fruit_purchased[fruit_name]
    print(fruit_name,"|",fruit_price,"|",fruit_no,"|",fruit_bill)

print("total bill :",total_bill)
print(fruit_inventory)

