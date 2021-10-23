# 정수와 배열을 한줄에 입력 받는 방법
# N, *arr = map(int, input().split())

# 문자열에서 한 문자씩 배열에 저장하는 방법
# n = int(input())
# arr = [list(input()) for _ in range(n)]

# 배열 연결해서 출력 1
# arr = [1, 2, 3, 4]
# print("".join(map(str, arr)))

# 배열 연결해서 출력 2(for 문을 작성할 필요가 없다)
# arr = [1, 2, 3, 4]
# print(*arr)
# 출력 결과 => (1 2 3 4)

# set 자료구조를 통해 리스트에 중복 원소 제거
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ]
# alpha = list(set(alpha))

# set 자료형으로 2차원 배열 중복 원소 제거(set 자료형은 1차원 배열에서는 적용되는데 2차웝 부터는 안되므로 tuple로 바꿔서 중복제거)
# lst = [[1, 2], [1,2], [1]]
# lst = list(set(map(tuple, lst)))
# lst = list(map(list, lst)) # 튜플 형태를 리스트 형태로 다시 변환