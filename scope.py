x = 25

def my_func():
    x = 50

my_func()

print(x)

name = 'Jhon Doe'

def greet():
    global name
    name = 'Ramesh'

    def hello():
        print('hello '+name)

    hello()

greet()

print(name)