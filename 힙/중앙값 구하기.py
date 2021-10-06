from sys import stdin
import heapq

case = int(input())
for _ in range(case):
    num = int(stdin.readline().strip())
    data = []
    for _ in range(int(num / 10) + 1):
        data.append(list(map(int, stdin.readline().split())))
    sum_data = sum(data, [])

    print(int(num / 2) + 1)
    for i in range(len(sum_data)):
        if i % 2 == 0:
            result = sum_data[0:i + 1]
            heapq.heapify(result)
            for _ in range(int(i / 2)):
                heapq.heappop(result)
            print(result[0], end=' ')
            result = []

            if (i // 2) == 9 or (i // 2) % 10 == 9:
                print()
    print()
