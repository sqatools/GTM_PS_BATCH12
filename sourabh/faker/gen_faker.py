from gen_faker import Faker

fk = Faker()


for i in range(1, 50):
    print(i)
    print("First Name: " + fk.first_name())
    print("Last Name: " + fk.last_name())
    print("Email: " + fk.email())
    print("Phone: " + fk.phone_number())
    print("Creditcard Number: " + fk.credit_card_number())
    print("Country name: " + fk.country())


    with open("user_data.txt", "a+") as file:
        data = f"{fk.first_name()}, {fk.last_name()}, {fk.email()}, {fk.phone_number()}, {fk.credit_card_number()}\n"
        file.write(data)

    print("-" * 50)


print(dir(fk))