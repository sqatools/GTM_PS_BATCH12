##### *args parameter ########
# args accepts the values in the form of tuple

def get_addition_values(num, *args):
    print(f"square of value :{num} :", num**2)
    print("args :", args)
    sum_value = 0
    for val in args:
        print(val)
        sum_value = sum_value + val


    print("addition of values :", sum_value)


#get_addition_values(3, 5, 6)
get_addition_values(3, 5, 6, 7, 8, 22, 44, 66)

print("_"*50)
#################################################
# *kwargs: Parameters :  This parameter accepts the values in form of key value format and as dict data

def get_user_info(**kwargs):
    print("user info:", kwargs)


get_user_info(fisrt_name='Rahul', last_name='Gupta', Age=35, address="Pune", email="rahul.gupta@gmail.com")
# user info: {'fisrt_name': 'Rahul', 'last_name': 'Gupta', 'Age': 35, 'address': 'Pune', 'email': 'rahul.gupta@gmail.com'}


print("_"*50)
def check_login(**kwargs):
    db_user = "user1@facebook.com"
    db_password = "Test@123"
    if kwargs['username'] == db_user and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Invalid credentials")


# check_login(username='user2@facebook.com', password="Test@123")
# Invalid credentials
check_login(username='user1@facebook.com', password="Test@123")
# Login Successful