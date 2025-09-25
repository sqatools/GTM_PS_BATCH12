import sqlite3
from faker import Faker
fk = Faker()

# create connection with database
def create_connection():
    con = sqlite3.connect("students.db")
    return con


def run_query(con, query):
    con.execute(query)


def run_select_query(con, query):
    data = con.execute(query)
    return data


##### initiate the connection with database and store in a variable #####
connection = create_connection()

# ######## run query to create a table  #####################
create_table_query = """create table student_info(name char[10], email char[20], phone char[20], address  char[20])"""
#run_query(connection, create_table_query)

# ######## run query to insert data to a table  #####################
# insert_data_query = """insert into student_info(name, email, phone, address) values('rahul', 'dravid', '6575665756', 'Bangalore')"""
# run_query(connection, insert_data_query)
# connection.commit()


################ Create 50 users details and insert data to the table ######################

# for i in range(1, 50):
#     print(i)
#     first_name = fk.first_name()
#     email = fk.email()
#     phone = fk.phone_number()
#     address = fk.address()
#     insert_data_query = f"""insert into student_info(name, email, phone, address) values('{first_name}', '{email}', '{phone}', '{address}')"""
#     #run_query(connection, insert_data_query)
#     connection.commit()


#select_query = "select * from student_info"
select_query = "select name, email  from student_info"
user_data = run_select_query(connection, select_query)
for val in user_data:
    print(val)

connection.close()