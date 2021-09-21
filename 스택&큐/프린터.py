priorities = list(map(int, input().split()))
location = int(input())

cnt = 0
while len(priorities) != 0:
    if location == 0:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            location = len(priorities) - 1
        else:
            cnt += 1
            break
    else:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            location -= 1
        else:
            priorities.pop(0)
            location -= 1
            cnt += 1

print(cnt)

# 틀렸음
'''
1. priorities 배열에 각각의 item 들이 모두 다르면 상관없지만 같은 것이 여러개 존재한다면 문제가 생기기 때문에 location = 0
(priorities[0]가 출력을 할지 말지 결정 하는 구간 이므로)일때 처리해 주도록 한다
2. location == 0일때 priorities[0] 값이 max(priorities)보다 작으면 그 item은 맨뒤로 가고 location도 끝 index가 된다
3. max(priorities)보다 크거나 같으면 출력된 횟수(cnt) + 1 해주고 break 걸어준다
4. location != 0 일때는 먼저 location == 0이 되는게 첫 번째 목표이고 priorities[0] 값이 max(priorities)보다 작으면
똑같이 뒤로 가고 location도 앞으로 가므로 location -= 1이 된다
5. max(priorities)보다 크거나 같으면 priorities[0]를 pop 해주고 그러므로 location -= 1이 되고 출력 되었으므로 cnt += 1가 된다'''