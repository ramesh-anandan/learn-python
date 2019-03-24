x = 'ramesh'

print(x[0]) #access index
print(x[-1]) #access last item of the string

#substring
print(x[2:]) 
print(x[:3])
print(x[2:4])
print(x[::2])

print(x.upper());

print(x.capitalize());

x = 'hello world'

print(x.split())
print(x.split('o'))

#string formatting
x = "First Name: {}, Last Name: {}".format('Ramesh', 'Anandhan')

print(x)

x = "First Name: {x}, Last Name: {y}".format(x = 'Ramesh', y = 'Anandhan')

print(x)
