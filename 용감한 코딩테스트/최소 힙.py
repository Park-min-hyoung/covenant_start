from sys import stdin
import heapq

case = int(input())
min_heap = []
for _ in range(case):
    value = int(stdin.readline())

    if value == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, value)