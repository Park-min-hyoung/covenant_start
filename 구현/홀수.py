data = []
for _ in range(7):
    value = int(input())
    if value % 2 != 0:
        data.append(value)

value_sum = sum(data)
print(-1) if value_sum == 0 else print('%d\n%d' %(sum(data), min(data)))