class Animal():

    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')


class Dog(Animal):

    def __init__(self):
        print('Dog Created')

    def bark(self):
        print('Woof')


my_dog = Dog()

my_dog.eat()