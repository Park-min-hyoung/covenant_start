from collections import deque

def bfs(index):
    queue = deque()
    queue.append(numbers[index])
    queue.append(-numbers[index])

    while queue:
        if len(queue) == 2 ** (index + 1) and not sqrt_check[index + 1]:
            sqrt_check[index + 1] = 1
            index += 1
        if index == len(numbers):
            break

        v = queue.popleft()
        queue.append(v + numbers[index])
        queue.append(v - numbers[index])

    result = 0
    for i in queue:
        if i == target:
            result += 1

    return result


numbers = list(map(int, input().split()))
target = int(input())
sqrt_check = [0] * 21

print(bfs(0))

