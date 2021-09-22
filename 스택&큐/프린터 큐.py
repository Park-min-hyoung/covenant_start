case = int(input())

for _ in range(case):
    length, position = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0
    while len(data) != 0:
        if position == 0:
            if data[0] < max(data):
                data.append(data.pop(0))
                position = len(data) - 1
            else:
                cnt += 1
                break
        else:
            if data[0] < max(data):
                data.append(data.pop(0))
                position -= 1
            else:
                data.pop(0)
                position -= 1
                cnt += 1
    print(cnt)