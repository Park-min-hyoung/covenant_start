from collections import Counter

data = [int(input()) for _ in range(10)]
result = Counter(data).most_common()
print(sum(data) // 10)
print(result[0][0])
