data = list(map(int, input().split()))
result = [0] * len(data)

stack = []
for i, price in enumerate(data):
    while stack and price < data[stack[-1]]:
        j = stack.pop()
        result[j] = i - j
    stack.append(i)

# 배열의 item 중에 자기 보다 작은 에가 뒤에 없는 item 만 여기로 온다
while stack:
    j = stack.pop()
    result[j] = len(data) - j - 1

print(result)

'''
1. 첫번째 item은 stack = null 이므로 무조건 0을 append 해주고 두번째 부터는 stack에 값(이전 값들의 index)을 통해 이전의 값들이 크다면
result에 그 차이(i - j)만큼 값을 수정해준다.(stack의 top 값이 현재의 값보다 작을때 까지 반복한다)
2. data 배열의 item들은 자기자신을 기준으로 뒤쪽에 자기보다 큰 item이 없다면 result에 값을 할당 받지 못한 상태이므로
하나씩 stack에서 값을 뽑아낸다음 전체시간(len(data))에서 시작시간(j=stack의 top 값)과 1을 빼주므로 시간을 구한다(result에 값을 할당한다)'''

'''data = list(map(int, input().split()))
result = []

for i in range(len(data)):
    cnt = 0
    for j in range(i + 1, len(data)):
        cnt += 1
        if data[i] > data[j]:
            break
    result.append(cnt)

print(result)'''