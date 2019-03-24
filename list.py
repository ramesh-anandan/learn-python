mylist = ['ramesh', 'anandhan', 35, 10000.0, [100.0, 200.0, 300.5]]

print(mylist)

print(len(mylist))

#access last itme of the list
print(mylist[-1])

print(mylist[2:])

mylist.append('address')

print(mylist)

print(mylist[4][2])

matrix = [ [1,2,3], [4,5,6], [7,8,9]  ]

first_column = [row[0] for row in matrix]

print('print column in matrix')
print(first_column)