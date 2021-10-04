tickets = []
target_num = 0
target_ch = 'ZZZ'

for _ in range(3):
    a, b = input().split()
    tickets.append([a, b])

for i in range(len(tickets)):
    if tickets[i][0] == 'ICN' and tickets[i][1] <= target_ch:
        for j in range(len(tickets)):
            if tickets[i][1] == tickets[j][0]:
                target_num = i
                target_ch = tickets[i][1]
                break

answer = []
answer.append(tickets[target_num][0])
answer.append(tickets[target_num][1])
check = [0] * (len(tickets) + 1)
check[target_num] = 1
num = 0
target_value = 'ZZZ'
while True:
    if len(answer) == len(tickets) + 1:
        break

    for i in range(len(tickets)):
        if target_ch == tickets[i][0] and not check[i] and tickets[i][1] <= target_value:
            target_value = tickets[i][1]
            num = i

    answer.append(target_value)
    target_ch, target_value = target_value, 'ZZZ'
    check[num] = 1

print(answer)
