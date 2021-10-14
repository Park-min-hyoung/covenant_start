# stack을 이용해한 문제 풀이(정확도: 100%)
'''tickets = []
for _ in range(5):
    a, b = input().split()
    tickets.append([a, b])
tickets.sort(reverse=True)

routes = dict()
for t1, t2 in tickets:
    if t1 in routes:
        routes[t1].append(t2)
    else:
        routes[t1] = [t2]

start = ['ICN']
answer = []
while start:
    top = start[-1]

    if top not in routes or len(routes[top]) == 0:
        answer.append(start.pop())
    else:
        start.append(routes[top].pop())

answer.reverse()
print(answer)'''

# DFS 이용해서 풀이(정확도: 75%)
'''def dfs(i, tickets, visited, depth, answer):
    visited[i] = 1
    answer.append(tickets[i][0])

    if depth == len(tickets) - 1:
        answer.append(tickets[i][1])
        return
    else:
        for k in range(len(tickets)):
            if not visited[k] and tickets[i][1] == tickets[k][0]:
                dfs(k, tickets, visited, depth + 1, answer)

tickets.sort()
for i, ticket in enumerate(tickets):
    if ticket[0] == 'ICN':
        answer = []
        visited = [0] * len(tickets)
        dfs(i, tickets, visited, 0, answer)
        
        if len(answer) == len(tickets) + 1:
            break

print(answer)'''

# 틀렸음
'''
1) stack 방법(x)
1. tickets 배열을 내림차순으로 정렬 해준 다음 for문을 돌면서 dict 자료구조를 이용해 key 값이 dict 변수(routes)에 없다면 
key값과 value를 dict에 추가해준다. key 값이 dict 변수에 있다면 해당 key 값의 value에 새로운 value를 append 해준다
(append 하기 위해서는 처음 key값과 value 값을 추가할때 value를 리스트로 추가해준다)
2. 시작이 'ICN'이기 때문에 start=['ICN']로 해주고 start가 빌때 까지 while 문을 돈다
3. while 문에서는 stack 자료구조의 성질을 이용해 가장 위의 값(top)이 routes의 key 값으로 설정되어 있지 않거나
설정 되어있더라도 value의 값 개수가 0개 일때 start 리스트에서 pop을 통해 뽑아낸 다음 answer에 넣어준다
4. 3번 조건에 반대라면 routes에 top과 같은 key 값도 설정되있고 그 key 값에 value 값이 1개 이상 있을 것이므로 
value값을 pop(가장 뒤의 값을 가져온다)한 다음 start에 넣어줌으로써 routes에 value 값을 제거해주는 작업을 반복한다
그리고 다 제거되면 3번 조건을 반복함으로써 answer를 구할 수 있다
5. 마지막으로 answer을 한번 더 뒤집어 준다

2) dfs 방법(x)
1. tickets를 오름차순으로 정렬해줌으로써 출발점이 'ICN'이 두개가 있더라도 도착점이 알파벳 순으로 빠른것이 선택될 것이다.
2. 출발점이 'ICN'인 것이 선택되면 enumerate(for문 문법)를 이용해 전달인자 타켓 번호, 항공권 정보 배열, 방문 배열, 
수행 횟수, 결과 배열을 전달해 dfs 메소드를 호출한다.
3. 방문을 했으면 체크해주고 결과 배열에 그 값을 넣어준다
4. 수행횟수 조건이 만족되면 dfs 함수를 탈출한다
5. 4번 조건에 반대라면 for 문을 통해 항공권 정보 배열에서 현재의 도착점과 다음 출발점이 같은지를 확인하고
같다면 수행횟수가 +1로 해주고 dfs 함수를 다시 호출한다.
6. 만약 항공권 정보 배열에서 'ICN' 3개가 있다고 가정하면 나머지 2개는 필요없으므로(어차피 알파벳 순으로 가장 빠른 도착점을 통해
dfs 함수를 수행시켰기 때문) 첫번째 'ICN'에 대해 dfs 함수가 수행된 후 결과 배열의 개수가 항공권 배열의 개수보다 크면 반복문을 탈출한다
(첫번째 'ICN'이 dfs 메소드를 돈 후 무조건 결과값의 개수 항공권 정보 개수보다 1이 크다는 보장이 없다 중간중간에 연결이 안되어 있을수도 있다.
그러므로 2번째가 수행되고 또 안되면 3번째로 인해 정상적으로 결과값이 출력이 될것이다, 결과 배열의 수가 항공 정보 배열의 수보다 1많다는 사실이
탐색이 끝났다는 말이다.
'''