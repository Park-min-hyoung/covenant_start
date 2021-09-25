height = list(map(int, input().split()))

result = 0
left, right = 0, len(height) - 1
left_height, right_height = height[left], height[right]

while left < right:
    left_height, right_height = max(left_height, height[left]), max(right_height, height[right])
    if left_height <= right_height:
        result += left_height - height[left]
        left += 1
    else:
        result += right_height - height[right]
        right -= 1

print(result)

# 틀렸음
'''
1. 양 끝쪽으로 각각 중간으로 오면서 빗물의 개수를 카운터 하면 되는 문제이다
2. 블럭의 이동을 위해 다음 위치에 이동한 후 max 함수를 통해 양 끝쪽의 높이를 최신화 해준다
=> 이동하는 Target(블럭)을 정하는 것도 목적이 있지만 빗물을 구하려면 높이 값(왼쪽 오른쪽 각각의 최대 높이)을 가지고 있어야 한다
3. 양 끝쪽의 각각의 해당 높이를 비교한다음 낮은 쪽이 움직일 수 있도록 구현한다(왼쪽이 낮으면 오른쪽으로 가고 오른쪽이 낮으면 왼쪽으로간다)
'''