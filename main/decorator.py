from functools import wraps
from time import perf_counter

'''
functions are first class object
'''


def my_decorator(func):
    '''Decorator Function'''

    @wraps(func)  # __name__ and __doc__ are changed to func
    def wrapper():
        # Do something before
        result = func()
        # Do something after
        return result

    return wrapper


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f' Duration {duration:.8f}s')
        return result

    return wrapper


@timer
def pfib(n):
    if n < 2:
        return n
    return pfib(n - 1) + pfib(n - 2)


# print(pfib(5))


'''
decorator in classes
'''
from functools import update_wrapper


class Count:

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        print(self.cnt)
        result = self.func(*args, **kwargs)
        return result


@Count
def cfib(n):
    if n < 2:
        return n
    return cfib(n - 1) + cfib(n - 2)


cfib(5)
