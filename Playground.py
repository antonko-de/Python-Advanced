from collections import deque as Deque

a = Deque()

a.append(1)
a.append(2)

a.popleft()
print(len(a))