from collections import deque

def bfs(queue):
    global time
    check_cnt = 0

    while queue:
        v = queue.popleft()
        if v == k:
            return 0
        queue.append(v - 1)
        queue.append(v + 1)
        queue.append(v * 2)

    time += 1
    bfs(queue)


n, k = map(int, input().split())
time = 0
queue = deque([n])
bfs(queue)

print(time + 1)