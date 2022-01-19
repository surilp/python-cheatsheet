from collections import deque

d = deque('abcdefg')

print(len(d))

for ele in d:
    print(ele)

d.pop()
d.popleft()
d.append(2)
d.appendleft(1)

print(d)


d.rotate(1)
print(d)