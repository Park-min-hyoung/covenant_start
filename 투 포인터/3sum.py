nums = list(map(int, input().split()))

result = []
end = 2

for start in range(len(nums) - 2):
    for middle in range(start + 1, len(nums) - 1):
        target_sum = nums[start] + nums[middle] + nums[end]
        if end == len(nums) - 1:
            if target_sum != 0 and end < len(nums):
                end += 1

            if target_sum == 0:
                value = [nums[start], nums[middle], nums[end]]
                value.sort()
                result.append(value)
            end += 1
        else:
            if target_sum != 0 and end < len(nums):
                end += 1

            while end < len(nums):
                target_sum = nums[start] + nums[middle] + nums[end]
                if target_sum == 0:
                    value = [nums[start], nums[middle], nums[end]]
                    value.sort()
                    result.append(value)
                end += 1

        if end == len(nums):
            end = middle + 2

        if middle == len(nums) - 2:
            end = start + 3

result.sort(key=lambda x: (x[0], x[1]))
solution = []
for v in result:
    if v not in solution:
        solution.append(v)

if len(nums) >= 3:
    print(solution)
else:
    print([])