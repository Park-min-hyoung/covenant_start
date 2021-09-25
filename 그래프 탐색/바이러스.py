def dfs(data, v, visited):
    global cnt
    cnt += 1
    visited[v] = True

    for i in data[v]:
        if not visited[i]:
            dfs(data, i, visited)

computer = int(input())
network = int(input())
data = [[] for _ in range(computer + 1)]
for _ in range(network):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (computer + 1)
cnt = 0

dfs(data, 1, visited)
print(cnt - 1)

'''from collections import deque

def bfs(data, start, visited):
    queue = deque([start])
    visited[start] = True
    global cnt

    while queue:
        v = queue.popleft()
        for i in data[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1


computer = int(input())
network = int(input())
data = [[] for _ in range(computer + 1)]
for _ in range(network):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (computer + 1)
cnt = 0

bfs(data, 1, visited)
print(cnt)'''