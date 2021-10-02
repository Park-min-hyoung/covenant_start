tickets = []
target_num = 0
target_ch = 'ZZZ'

for _ in range(3):
    a, b = input().split()
    tickets.append([a, b])

for i in range(len(tickets)):
    if tickets[i][0] == 'ICN' and tickets[i][1] <= target_ch:
        target_num = i
        target_ch = tickets[i][1]

answer = [''] * (len(tickets) + 1)
answer[0] = tickets[target_num][0]
answer[1] = tickets[target_num][1]
check = [0] * (len(tickets) + 1)
check[target_num] = 1
num = 0
target_ch2 = 'ZZZ'
while True:
    if len(answer) == len(tickets) + 1:
        break

    for i in range(len(tickets)):
        if target_ch == tickets[i][0] and not check[i] and tickets[i][1] <= target_ch2:
            target_ch2 = tickets[i][1]
            num = i

    answer[num] = target_ch2
    check[num] = 1

print(answer)
