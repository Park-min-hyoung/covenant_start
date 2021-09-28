from collections import deque

def bfs(queue, visited):
    global time
    old_check = 1
    new_check = 0

    while queue:
        v = queue.popleft()

        if v == k:
            return 0

        if not visited[v - 1]:
            queue.append(v - 1)
            visited[v - 1] = True
        if not visited[v + 1]:
            queue.append(v + 1)
            visited[v + 1] = True
        if not visited[v + 1]:
            queue.append(v * 2)
            visited[v * 2] = True
        new_check += 1

        if old_check == new_check:
            old_check = len(queue)
            new_check = 0
            time += 1


n, k = map(int, input().split())
time = 0
visited = [False] * 100001
visited[n] = True

bfs(deque([n]), visited)
print(time)