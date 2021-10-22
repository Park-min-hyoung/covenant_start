nums = list(map(int, input().split()))

result = []

nums.sort()
for start in range(len(nums) - 2):
    left, right = start + 1, len(nums) - 1

    if start > 0 and nums[start] == nums[start - 1]:
        continue

    while left < right:
        sum = nums[start] + nums[left] + nums[right]

        if sum > 0:
            right -= 1
        elif sum < 0:
            left += 1
        else:
            result.append([nums[start], nums[left], nums[right]])

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1

print(result)

# 틀렸음
'''
1. sort()를 통해 왼쪽 포인터가 이동되면 값이 커지고 오른쪽 포인터가 이동되면 값이 작아지는 방식을 이용했다
2. 시작점(start)를 한개씩 올려주면서 왼쪽점(left)과 오른쪽점(right)를 목표값에 따라 이동시켜주는 아이디어(투 포인터: left, right)
3. 이동할때 합(sum)이 0보다 크면 오른쪽점을 right - 1 작으면 왼쪽점을 left + 1 해주고 3가지의 값의 합이 목표값이 라면
배열에 추가해 준다
4. 배열에 추가한 후 중복 되는 배열 원소는 더해주지 않기 위해 left와 right를 수정해준다(만약 -1 -1 -1 -1 1 라는 리스트가 있다면
첫번째(start) 두번째(left) 다섯번째(right)에 의해 결과 배열에 원소가 들어갔을 것이다. 그 다음은 세번째 -1이 선택되더라도
어차피 결과 배열에 추가 될때는 같은 값이므로 배열[left] != 배열[left + 1]일때까지 left를 오른쪽으로 옮겨주고 반대로
배열[right] != 배열[right - 1]일때까지 right를 왼쪽으로 옮겨준다
5. start에 해당하는 반복문을 돌때 nums의 현재 인덱스에 해당하는 값이 그전의 인덱스에 해당하는 값과 같다면 다음 시작점으로 넘어간다
(어차피 값이 같으면 목표값을 찾더라도 결과 배열에 추가되는 원소는 같음으로 인해 중복되기 때문에)
'''