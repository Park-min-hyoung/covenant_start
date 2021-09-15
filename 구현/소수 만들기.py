from itertools import combinations

nums = list(map(int, input().split()))
combo_nums = list(combinations(nums, 3))
cnt = 0

for value in combo_nums:
    sum_value = sum(value)
    for i in range(2, sum_value + 1):
        if i == sum_value:
            cnt += 1
            break
        if sum_value % i == 0:
            break

print(cnt)