# variable num of args

def addition(*args):
    return sum(args)


print(addition(1, 2, 3, 4))
print(addition(*[1, 2, 3, 4]))  # to send list put astrix before list

# lambda

cel_to_fah = lambda temp: (temp * 9 / 5) + 32
fah_to_cel = lambda temp: (temp - 32) * 5 / 9

ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

print(list(map(cel_to_fah, ctemps)))
print(list(map(fah_to_cel, ftemps)))



# keyword arguments

def myFunc(arg1, arg2, *, arg3 = "foo"): # astric forces anything after to be specified with its name when called
    pass

myFunc(1,2, arg3 = 'bar')


def myFunc2(*, arg1, arg2):
    pass
myFunc2(arg1 =1, arg2 =2)