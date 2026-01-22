from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
print(queue.popleft())
print(queue)
queue.appendleft(0)
print(queue)
print(queue.pop())
print(queue)