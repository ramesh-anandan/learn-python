import my_module
import my_module as mm
from my_module import fun_in_module


my_module.fun_in_module()

mm.fun_in_module()

fun_in_module()

if __name__ == '__main__':
    print('use_module is being run directly')
else:
    print('use_module is imported module')