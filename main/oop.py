class Person:
    # attribute initializer. Object is already created before this method is called
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__secret = None

    def get_name(self):
        return self.name

    def object_has_attribute(self, attr_name):
        return hasattr(self, attr_name)


p1 = Person("John", "Male")
p2 = Person("Jess", "Female")

print(p1.name)
print(p2.name)

print(p1.object_has_attribute("name"))
print(p1.object_has_attribute("gender"))
print(p1.object_has_attribute("email"))

# double underscore (name mangeling) if you don't subclass to override add __

# type
print(type(p1))
print(type(p1) == type(p2))
print(isinstance(p1, Person))
print(isinstance(p1, object))
print(issubclass(Person, object))


# class level method and members

# class method
class Book:
    BOOK_TYPE = ("HARDCOVER", "PAPERBACK", "EBOOK")

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPE


print(Book.BOOK_TYPE)

print(Book.get_book_types())


# static method - dont modifiy state of class or instance
# single design pattern

class Book:
    __booklist = None

    @staticmethod
    def get_book_list():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist


# inheritance
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.page = pages


# abstract class
from abc import ABC, abstractmethod  # ABC - abstract base class


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# g = GraphicShape()


class Triangle(GraphicShape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calcArea(self):
        return 0.5 * self.base * self.height


print(Triangle(1, 2).calcArea())

# multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


print(help(A))
C().show_props()
print(C.mro())  # method resolution order
print(C.__mro__)

# interface


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# g = GraphicShape()


class Triangle(GraphicShape, JSONify):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calcArea(self):
        return 0.5 * self.base * self.height

    def toJSON(self):
        pass


t = Triangle(1, 2)


# using composition
# has relationship

class Book:

    def __init__(self, author):
        self.author = author


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


# magic methods

'''
__str__(self) - string representation for user
__repr__(self) - developer facing string to recreate object
__eq__(self, other) - deep comparison
__ge__(self, other) - return if self is grater than or equal other
__lt__(self, other) - return if self is less than other
__getattribute__(self, name_attr)  - get attribute plus some logic
__setattr__(self, name_attr, value) - set attribute plus pre logic
__getattr__(self, attr_name) - is called with getattribute look up is failed
__call__(self, attr1, ..) - call the object like function
__add__(self, other) - custom add
__len__(self) - custom length
'''


class Magic:

    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        if item == "name":
            return super().__getattribute__("name") + "2"

    def __setattr__(self, key, value):
        if key == "name":
            if type(value) is not str:
                raise ValueError(
                    f"name is not str type but it is {type(value)}")
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return item + "does not exist"


m = Magic("Hello")
print(m.name)

m.name = 'hello'
x = m.hello
pass


# data classes
# python 3.7+ type hints are required
# automatically import repr and eq methods
from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float


b = Book("title", "author", 50, 10.0)
c = Book("title", "author", 50, 10.0)
print(b == c)

# post init function


def price_func():
    return 10


@dataclass
class Book:
    title: str = "No Title"  # default values - non default attr should be first
    author: str = "No AUthor"
    pages: int = 0
    price: float = field(default=0.0)
    price2: float = field(default_factory=price_func)

    def __post_init__(self):  # is called after defualt init is called in data class
        self.description = f"{self.title}, {self.author}"

# immutable data classes


@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: str = 0


x = ImmutableClass("hello", 15)
print(x)


# property decorator
'''
Allows your to treat method as property
'''


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


e = Employee('John', 'Doe')
print(e.email)
print(e.fullname)
e.fullname = 'Michal W'
print(e.fullname)
del e.fullname
print(e.first)
