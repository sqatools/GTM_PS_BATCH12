###pip install faker

from faker import Faker


fk = Faker()

for i in range (1,10) :
    print(i)
    print("first name :",fk.first_name())
    print("Last_name :",fk.last_name())


