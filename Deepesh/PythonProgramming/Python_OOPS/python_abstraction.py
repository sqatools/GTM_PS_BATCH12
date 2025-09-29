# str1 = "Hello"
# print(str1.upper())
#
"""
Abstraction :  When we hide the internal architecture of the code and show overview information to user, then it is called abstraction.
We can achive astraction, when we define method on parent class and implement in child.



"""
from abc import abstractmethod


class Animal:

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def food(self):
        pass

    @abstractmethod
    def breed(self):
        pass



class Dog(Animal):
    def name(self):
        print("Tommy")

    def voice(self):
        print("Bark")

    def food(self):
        print("Dog Food")

    def breed(self):
        print("German")


class Lion(Animal):
    def name(self):
        print("shera")

    def voice(self):
        print("Roar")

    def food(self):
        print("Meat")

    def breed(self):
        print("African Lion")


obj1 = Lion()
obj1.voice()