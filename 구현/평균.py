n = int(input())
data = list(map(int, input().split()))
max_score = max(data)
new_score = []

for i in range(n):
    new_score.append(data[i] / max_score * 100)

print(sum(new_score) / n)