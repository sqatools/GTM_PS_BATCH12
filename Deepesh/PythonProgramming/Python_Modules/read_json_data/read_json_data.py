import json


def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(data, type(data))
        # convert string data into dictionary
        json_content = json.loads(data)

    return json_content


# data = read_json_data("users_data.json")
# print(data, type(data))
#
# print("Phone :", data['phone'])
# print("email", data['email'])


def create_a_new_user(firstname, lastname, email, phone, address):
    print("First Name :", firstname)
    print("Last Name :", lastname)
    print("Email ID :", email)
    print("Phone Number :", phone)
    print("Address :", address)


user_data  = read_json_data("signup_data.json")
create_a_new_user(firstname=user_data['firstname'],
                  lastname=user_data['lastname'],
                  email=user_data['email'],
                  phone=user_data['phone'],
                  address=user_data['address'])