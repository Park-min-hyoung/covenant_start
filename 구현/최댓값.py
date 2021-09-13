from sys import stdin

data = list(int(stdin.readline().strip()) for _ in range(9))
value = data[0]
index = 0

for i in range(1, 9):
    if data[i] > value:
        value = data[i]
        index = i

print(value)
print(index + 1)

'''data = []
for _ in range(9):
    data.append(int(input()))

print(max(data))
print(data.index(max(data)) + 1)'''