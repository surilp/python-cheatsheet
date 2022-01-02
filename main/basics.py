my_int = 5
my_float = 13.2
my_str = "this is a string"
my_bool = True
my_list = [0, 1, "two", 3.2, False]
my_tuple = (0, 1, 2)
my_dict = {"one": 1, "two": 2}

print(my_int)
print(my_float)
print(my_str)
print(my_bool)
print(my_list)
print(my_tuple)
print(my_dict)

# list slicing
start = 1
end = 5
step = 5
my_list[start:end:step]  # start is included and end is excluded

# reverse list
my_list[::-1]  # default start and end (entire sequence) but step will be - 1


# global vs local
def func_local():
    my_str = "local var"
    print(my_str)


def func_global():
    global my_str
    my_str = "local var"
    print(my_str)


print(my_str)
func_local()
print(my_str)

print(my_str)
func_global()
print(my_str)

# delete from memory
del my_str


# variable number of arguments
def multi_add(*args):  # * args has to be last parameter
    result = 0
    for num in args:
        result += num
    return result


# 3.10 case statements
value = "one"

match value:
    case "one":
        result = 1
    case "two":
        result = 2
    case "three" | "four":
        result = (3, 4)
    case _:
        result = -1


# find out python version at runtime
import platform
print(platform.python_version())