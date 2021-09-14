n = int(input())
data = list(map(int, input().split()))
max_value = -1000000
min_value = 1000000

for i in range(n):
    if data[i] < min_value:
        min_value = data[i]
    if data[i] > max_value:
        max_value = data[i]

print(min_value, max_value)

n = int(input())
data = list(map(int, input().split()))

print(min(data), max(data))