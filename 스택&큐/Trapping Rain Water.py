height = list(map(int, input().split()))
h = height[0]
stack = []

check = False
cnt = 0
for i in range(1, len(height)):
    if height[i] >= h:
        while stack:
            if check:
                cnt += (height[i] - height[stack.pop(0)])
            else:
                cnt += (h - height[stack.pop(0)])
        if height[i] != max(height):
            h = height[i]
    else:
        stack.append(i)
        if i - 1 == 0 and height[i - 1] == max(height):
            h = height[i]
            check = True

print(cnt)