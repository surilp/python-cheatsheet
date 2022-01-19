from collections import defaultdict

fruits = ['apple', ' pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

fruit_dict = defaultdict(lambda: 100)

for fruit in fruits:
    fruit_dict[fruit] += 1

print(fruit_dict)


