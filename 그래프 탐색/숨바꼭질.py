from collections import deque

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

MAX = 10 ** 5
n, k = map(int, input().split())
visited = [0] * 100001

bfs()

# 틀렸음
'''
1. BFS 문제로써 deque 자료구조를 사용한다
2. 층 마다 카운터를 어떻게 올릴지 고민을 했었는데 역시 방법이 있었다.
3. bfs 함수 안에서 queue(deque 사용)에다가 출발 숫자를 append 해주고 queue 안에 데이터가 없을때 까지 while문을 돌려준다
4. bfs 알고리즘 특성 상 queue에서 가장 먼저 들어온 데이터를 뽑아내고(popleft()) 그 데이터 값이 목표 데이터 값이랑 같으면 visited[데이터]를 통해
진행된 횟수(층수 라고 생각해도 될듯, 1부터 시작해서 밑으로)
5. 그리고 for 문(for nx in(x - 1, x + 1, x * 2), for문을 이렇게 사용하는 것은 처음봤다...)을 사용해서 3종류의 값이 조건을 만족하면
visited[nx] = visited[x] + 1과 queue에 nx를 append 한다.
6. visited[x] 같은 경우 visited[nx]의 위층 데이터이므로 위층이 1층이면 0 + 1 = 1, 2층이면 1 + 1 = 2가 될것이므로 
계속 누적된 값이 더해지므로 층수(진행된 횟수)가 한칸 내려감에 따라 1이 더해진다. 그리고 한번 방문한 곳은 무조건 데이터가 1이상이므로
not visited[nx]를 통해 중복 방문하지 않게 하므로 메모리 초과를 방지할 수 있다
'''