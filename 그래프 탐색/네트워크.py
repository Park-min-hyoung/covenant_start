def dfs(computers_data, v, visited):
    if visited[v - 1]:
        return False

    visited[v - 1] = True

    for i in computers_data[v]:
        if not visited[i - 1]:
            dfs(computers_data, i, visited)

    return True


n = int(input())
computers = []
for _ in range(n):
    a, b, c = map(int, input().split())
    computers.append([a, b, c])

computers_data = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and computers[i - 1][j - 1] == 1:
            computers_data[i].append(j)

answer = 0
visited = [False] * n

for i in range(1, n + 1):
    value = dfs(computers_data, i, visited)
    if value:
        answer += 1

print(answer)

