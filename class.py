class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi


my_cirlce = Circle(2)

print(my_cirlce.area())

# Class special methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'title: {}, author: {}, pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print(self.title + ' is deleted')


b = Book('Udemy Python', 'Jhon Doe', 200)

print(b)

print(len(b))

del b    