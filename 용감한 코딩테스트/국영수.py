from sys import stdin

case = int(input())
score = []
for _ in range(case):
    value = list(stdin.readline().split())
    score.append([value[0], int(value[1]), int(value[2]), int(value[3])])

score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for result in score:
    print(str(result[0]))