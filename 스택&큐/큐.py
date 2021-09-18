from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
queue = deque([])
for _ in range(n):
    command = list(stdin.readline().split())

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front' or command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        elif command[0] == 'front':
            print(queue[0])
        else:
            print(queue[-1])