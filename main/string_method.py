
'''
string - sequence of unicode character
bytes - sequence of 8 bit value
'''

# sequence of byte
b = bytes([0X41, 0X42, 0X43, 0X44])
print(b)

# sequence of unicode character
s = "This is a string"
print(s)

# combine - decode byte to string
# decode - byte to string
# encode - string to byte
print(s + b.decode('utf-8'))
print(b + 'hello'.encode('utf-8'))


string = "123"

string.isupper()
string.islower()
string.isalnum()
string.isalpha()


# String template
from string import Template
author = "SP"
title = "My Title"
str1 = Template("${author} and ${title}")
str2 = str1.substitute(author=author, title= title)
print(str2)