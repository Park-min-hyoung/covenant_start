import heapq
from sys import stdin

case = int(input())
max_heap = []
for _ in range(case):
    value = int(stdin.readline().strip())

    if value == 0:
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, (-value, value))