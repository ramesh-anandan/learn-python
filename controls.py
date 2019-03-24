# if else flow

x = 1
y = 2

if x != y and y > 1:
    print('x != y and y > 1')

if x == y:
    print('x == y')
elif x > y:
    print('x > y')
else:
    print('x < y')

# for loop

x = ['ramesh', 'haasini' ,'medha']

for item in x:
    print(item)

y = {'name':'ramesh', 'age': 35, 'profession': 'software'}

for item in y:
    message = '{}: {}'.format(item, y[item])
    print(message)

for item in y.values():
    print(item)

my_list = list(range(1,5))
out = [num**2 for num in my_list]
print(out)

# tuples in loop

x= [('ramesh','35'),('haasini','7'),('medha','4')]

for name, age in x:
    print(name, age)