car1_brand = "Tesla"
car1_model = "Model S"

car2_brand = "BMW"
car2_model = "X5"

print(car1_brand, car1_model)
print(car2_brand, car2_model)

print("_"*60)
#########################################
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = car("tesla", "Model S")
car2= car("BMW", "X5")

print(car1.brand,car1.model)
print(car2.brand,car2.model)
##############################################
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i)
print("_"*50)
################################3
str1 = "We aRe Learning python Programing"
cap = ""

for i in str1:
    if i.isupper():
        print(i)
        cap = cap + i
print(cap)