from sys import stdin
import heapq

def solution():
    min_heap = []
    max_heap = []
    middle = data[0]
    result = [middle]

    for i, val in enumerate(data[1:], 1):
        if val <= middle:
            heapq.heappush(min_heap, -val)
        else:
            heapq.heappush(max_heap, val)

        if i % 2 == 0:
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, middle)
                middle = -heapq.heappop(min_heap)
            elif len(min_heap) < len(max_heap):
                heapq.heappush(min_heap, -middle)
                middle = heapq.heappop(max_heap)

            result.append(middle)

    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
        if i % 10 == 9:
            print()
    print()

case = int(input())
for _ in range(case):
    num = int(stdin.readline().strip())
    data = []
    if num % 10 == 0:
        for _ in range(num // 10):
            data.extend(list(map(int, stdin.readline().split())))
    else:
        for _ in range(num // 10 + 1):
            data.extend(list(map(int, stdin.readline().split())))

    solution()

# 틀렸음(x)
'''
1. list에 append 말고 extend 사용하면 list를 넣어줘도 [] 있는채로 안들어가고 값만 들어간다
2. idx, value for in enumerate(list나 value, 시작번호) 이용하는 개념, 시작번호를 조작할 수 있다 
3. 처음부터 반복문을 돌면서 list를 heap로 바꿔준 다음 heappop으로 출력하는 방법이 있지만 이 방법은 시간이 너무 오래걸린다...
4. middle 값을 통해 새로 조회하는 값이 middle 보다 크면 maxh(최소 heap), 작으면 minh(최대 heap)에 넣어주고 홀 수 일때마다
두 힙의 길이를 비교한다
5. 홀 수 일때 두 힙의 데이터 개수의 합은 짝수 이므로 maxh의 개수가 minh의 개수보다 많을경우에는 maxh(최소 heap)의 가장 첫번째 값이
middle 값이다(이전의 middle 값은 -부호를 달고 minh(최대 heap)로 들어간다
6. maxh의 개수가 minh의 개수보다 작을 경우 minh(최대 heap)의 가장 첫번째 값의 부호 반대 값이 middle 값이다
(이전의 middle 값은 maxh(최소 heap)으로 들어간다'''


# 4000ms 걸린다...(거의 3중 for문)
# from sys import stdin
# import heapq
#
# case = int(input())
# for _ in range(case):
#     num = int(stdin.readline().strip())
#     data = []
#     for _ in range(int(num / 10) + 1):
#         data.extend(list(map(int, stdin.readline().split())))
#
#     print(int(num / 2) + 1)
#     for i in range(0, len(data), 2):
#         result = data[0:i + 1]
#         heapq.heapify(result)
#         for _ in range(int(i / 2)):
#             heapq.heappop(result)
#         print(result[0], end=' ')
#         result = []
#
#         if (i // 2) == 9 or (i // 2) % 10 == 9:
#             print()
#     print()