### args parameter ####
#args accepts the values in the from of tuple
def get_addition_values(*args):
    print("args:",args)
    sum_value=0
    for val in args:
        print(val)
        sum_value=sum_value+val

    print("addition of values:",sum_value)
get_addition_values(3,5,6)
"""
args: (3, 5, 6)
3
5
6
addition of values: 14
"""
def get_addition_values(num,*args):
    print(f"square of value:{num}:",num**2)
    print("args:",args)
    sum_value=0
    for val in args:
        print(val)
        sum_value=sum_value+val
    print("addition of values:",sum_value)
get_addition_values(3,5,6,7,8,22,44,66)
"""
args: (5, 6, 7, 8, 22, 44, 66)
5
6
7
8
22
44
66
addition of values: 158
"""
### kwargs parameter
def get_user_info(**kwargs):
    print("user info:",kwargs)
get_user_info(first_name='rahul',last_name='gupta',age=35,address="pune",email="rahul@gmail.com")
#user info: {'first_name': 'rahul', 'last_name': 'gupta', 'age': 35, 'address': 'pune', 'email': 'rahul@gmail.com'}
print("_"*50)

def check_login(**kwargs):
    db_user="user1@facebook.com"
    db_password="Test@123"
    if kwargs['username']==db_user and kwargs['password']==db_password:
        print("login successful")
    else:
        print("invalid credentials")
check_login(username='user2@facebook.com',password="Test@123")
# invalid credentials
check_login(username='user1@facebook.com',password="Test@123")
# login successful


