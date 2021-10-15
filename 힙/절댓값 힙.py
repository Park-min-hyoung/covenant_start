import heapq
from sys import stdin

case = int(input())
abs_heap = []
for _ in range(case):
    value = int(stdin.readline().rstrip())

    if value == 0:
        if not abs_heap:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])
    else:
        heapq.heappush(abs_heap, (abs(value), value))