def new_decorator(func):

    def wrap():
        print('before')

        func()

        print('after')

    return wrap


@new_decorator
def func_need_decorator():
    print('i need decorator')

func_need_decorator()


# global/locals: Accessing global/local variables from dictionary

def localFunction():
    varLocal = 10;
    print(locals())
    print(globals())

localFunction();