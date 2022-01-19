from collections import Counter

fruits = ['apple', ' pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

c1 = Counter(fruits)
print(c1['apple'])


print(sum(c1.values()))

c1.update(fruits)
print(c1["apple"])


print(c1.most_common(3))

c1.subtract(fruits)
print(c1['apple'])


#print(c1 & c2) common between two counters