def get_addition_values(*args):
    print("agrs:", args)
    sum_value = 0
    for val in args:
        print(val)
        sum_value = sum_value+val
    print("addition of values:", sum_value)
get_addition_values(3,5,7,8,10,100)

print("_"*60)


def check_login(**kwargs):
    db_user = "user1@facebook.com"
    db_password = "Test@123"
    if kwargs['username'] == db_user and kwargs['password'] == db_password:
        print("login successfull")
    else:
        print("invalid successfull")


check_login(username='user1@facebook.com', password='Test@123')
