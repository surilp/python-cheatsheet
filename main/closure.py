def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func()


outer_func()


def outer_func_v2():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func_v2()
print(my_func.__name__)


def outer_func_v3(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func_v3("hi")
hello_func = outer_func_v3("hello")

hi_func()
hello_func()


def add(a, b):
    return a + b


def logger(func):
    def inner_func(*args):
        print('logging')
        return func(*args)

    return inner_func


new_add = logger(add)
print(new_add(1, 2))
