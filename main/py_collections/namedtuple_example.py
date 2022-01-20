import collections

Point = collections.namedtuple("Point", "x y")


p1 = Point(10, 20)
p2 = Point(30,40)

print(p1)
print(p2)

print(p1.x)
print(p2.y)


p1 = p1._replace(x = 100) # creates new instance
print(p1)



Color = collections.namedtuple('Color', ['red', 'green', 'blue'])

