def display(message='welcome'):
    """
    prints the message on console
    """
    a = "Param: {}".format(message)
    print(a)


display()

# result result
def addNum(num1, num2):
    return num1+num2


result = addNum('2','3')

print(type(result))

# lamda expression
my_list = list(range(1,9))

result = filter(lambda num:num%2 == 0, my_list)
print(list(result))
