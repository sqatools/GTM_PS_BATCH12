"""
Encapsulation and Data Hiding :  When we combine class member as single unit and restrict data to access outside the class then it is called encasulation.


"""


class Car:
    def __init__(self, car_name, car_price, car_comp):
        self.car_name = car_name     # normal instance variable
        self._car_price = car_price  # variable with single underscore as prefix
        self.__car_comp = car_comp   # double underscore as prefix

    def show_car_name(self):
        print(f"Car name: {self.car_name}")

    def _show_car_price(self):
        print(f"car price: {self._car_price}")

    def __show_car_company(self):
        print(f"Car company: {self.__car_comp}")


obj = Car("Harrier", "20 Lac", "TATA")

# -> If we define any variable/method with single/double underscore as prefix, then it does not
#    show in suggestion list.
#  ->  Suggestion will only show variable/method without single or double underscore.

obj.show_car_name()

# When we want to access any method/variable with single underscore as prefix, then we can directly access it
# but it doesn't visible is suggestion  list
obj._show_car_price()


# When we want to access any method/variable with double underscore as prefix, then we can not access directly
# we have to follow the pattern to provide class with single underscore and method/variable name with double underscore

obj._Car__show_car_company()


print(dir(Car))

# '_show_car_price', 'show_car_name', '_Car__show_car_company'