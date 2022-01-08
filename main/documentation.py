print(map.__doc__)


import collections
print(collections.__doc__)

'''
Enclose docstring in triple quotes
First line should be summary sentence of functionality
Modules: List important classes, functions, exceptions
Classes: List important methods
Functions: List parameters and explain each, one per line
    if there is return value, list it, otherwise omit
    mention exceptions it can raise
'''

def myFunc(arg1, arg2 = None):
    """myFunc(arg1, arg2 = None) --> does nothing

    :param arg1:
    :param arg2:
    :return:
    """
    print(arg1, arg2)


print(myFunc.__doc__)