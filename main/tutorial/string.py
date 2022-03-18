message1 = "the \" message"
message2 = "John's car"

print(message1)
print(message2)


multi_line_message = """multi line message
                        multi line message 2
                    """
print(multi_line_message)


num_char = len(message1)
print('number of character in message1', num_char)


print('lower case', message1.lower())
print('upper case', message1.upper())
print('count message in message', message1.count("s"))
print('find index of s', message1.index("s"))


# replace
new_message = message1.replace("message", "messages")
print(new_message)

print(dir(message1))
print(help(str))
print(help(str.lower))
