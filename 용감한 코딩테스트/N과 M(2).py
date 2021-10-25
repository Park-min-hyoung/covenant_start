from itertools import combinations

n, m = map(int, input().split())
data = list(str(i) for i in range(1, n + 1))

for result in list(combinations(data, m)):
    print(' '.join(result))