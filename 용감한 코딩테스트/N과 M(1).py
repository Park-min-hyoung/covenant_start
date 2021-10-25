from itertools import permutations

n, m = map(int, input().split())
data = [str(i) for i in range(1, n + 1)]

for result in list(permutations(data, m)):
    print(" ".join(result))