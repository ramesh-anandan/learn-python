def fun_in_module():
    print('Function inside my_module')


if __name__ == '__main__':
    print('my_module is being run directly')
else:
    print('my_module is imported module')