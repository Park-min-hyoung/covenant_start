import heapq

T = int(input())
L = list(map(int, input().split()))
heapq.heapify(L)

while len(L) >= 2:
    m = heapq.heappop(L)

    if m >= T:
        print(m)
        break

    else:
        ms = heapq.heappop(L)
        heapq.heappush(L, m + ms)

# https://littlefoxdiary.tistory.com/3