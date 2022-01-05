list1 = [1, 2, 3, 0, 5, 6]

print(any(list1))  # atleast one evaluate to true
print(any(list1))  # all evaluate to true

print(min(list1))
print(max(list1))
print(sum(list1))

days = ["sun", "mon", "Tue", "wed", "Thu", "fri", "sat"]
days_in_fr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "ven", "sam"]

# iterator
i = iter(days)
x = next(i)
while x:
    print(x)
    try:
        x = next(i)
    except StopIteration as err:
        x = None


def func():
    for i in range(5):
        yield i


x = iter(func, '')  # sentinal value = '' iterator stops

# enumerate
for i, day in enumerate(days, start=1):
    print(i, day)

# zip
for i, (day, f_day) in enumerate(zip(days, days_in_fr), start=1):
    print(i, day, f_day)

# transform
nums = (1, 8, 4, 5, 13, 26, 381, 4100, 58, 47)
chars = "abcDeFGHiJklmnoP"
grades = (81, 89, 94, 78, 61, 66, 99, 74)

# fitler
print(list(filter(lambda x: x % 2 != 0, nums)))
print(list(filter(lambda x: x.islower(), chars)))

#map
print(list(map(lambda x: x**2, nums)))
print(list(map(lambda x: 'a' if x > 90 else 'b', grades)))


#itertools
from itertools import cycle, count,accumulate, chain, dropwhile, takewhile

#cycle - inifinite loop
seq1 = ["Joe", "John", "Mike"]
c = cycle(seq1)
for item in c:
    print(item)
    break

#count
c = count(start = 100, step = 10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

#accumulate
vals = [10,20,30,40,50,60,70]
a = accumulate(vals)
print(list(a))

vals = [10,20,30,40,50,30,400]
a = accumulate(vals, func= max)
print(list(a))

#chain
x = chain('abcd', '1234')
print(list(x))

#dropwhile - drop while test func return True and return every value after that
print(list(dropwhile(lambda x : x < 40, vals)))

#takewhile
print(list(takewhile(lambda x : x < 40, vals)))