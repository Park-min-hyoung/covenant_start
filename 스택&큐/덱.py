from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
date = deque()
for _ in range(n):
    command = stdin.readline().split()

    if command[0] == 'push_front':
        date.appendleft(command[1])
    elif command[0] == 'push_back':
        date.append(command[1])
    elif command[0] == 'pop_front':
        if len(date) == 0:
            print(-1)
        else:
            print(date.popleft())
    elif command[0] == 'pop_back':
        if len(date) == 0:
            print(-1)
        else:
            print(date.pop())
    elif command[0] == 'size':
        print(len(date))
    elif command[0] == 'empty':
        if len(date) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(date) == 0:
            print(-1)
        else:
            print(date[0])
    elif command[0] == 'back':
        if len(date) == 0:
            print(-1)
        else:
            print(date[-1])