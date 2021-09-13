n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[0] * data[n - 1])

# 틀렸음
'''
1. 입력은 내가 작성한 테스트 케이스처럼 오름차순으로 입력되지 않는다
2. 만약 12의 진짜 약수는 2, 3, 4, 6인데 입력은 (6 4 2 3) 이런식으로 무작위로 입력이 들어오므로 정렬 후 계산'''