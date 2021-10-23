n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x:(x[0], x[1]))

for result in data:
    print(result[0], result[1])