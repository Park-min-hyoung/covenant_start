N, K = map(int, input().split())
data = [i for i in range(1, N + 1)]

answer = []
num = 0

for _ in range(N):
    num += K - 1
    if num >= len(data):
        num = num % len(data)

    answer.append(str(data.pop(num)))

print('<', ', '.join(answer), '>', sep='')

# 0.8초 소요(위에 풀이는 0.15초 소요 6~7배 차이)
'''n, k = map(int, input().split())

people = []
for i in range(1, n + 1):
    people.append(i)

target = -1
result = []
check = [0 for _ in range(n)]
while True:
    cnt = k
    while True:
        target += 1
        if target >= n:
            target = 0

        if check[target] == 0:
            cnt -= 1

        if cnt == 0:
            result.append(str(people[target]))
            check[target] = 1
            break

    if len(result) == n:
        break

print("<", ", ".join(result)[:], ">", sep='')'''