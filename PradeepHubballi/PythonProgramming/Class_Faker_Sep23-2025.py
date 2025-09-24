###pip install faker

from faker import Faker


fk = Faker()

for i in range (1,10) :
    print(i)
    print("first name :",fk.first_name())
    print("Last_name :",fk.last_name())
    with open("user_data.txt", "a+") as file:
        data = f"{fk.first_name()}, {fk.last_name()}, {fk.email()}, {fk.phone_number()}, {fk.credit_card_number()}\n"
        file.write(data)
    print("_"*50)

print(dir(fk))