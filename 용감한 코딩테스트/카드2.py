from collections import deque
import time
start_time = int(round(time.time() * 1000))

num = int(input())
data = deque([int(i) for i in range(1, num + 1)])

while len(data) > 1:
    data.popleft()
    data.rotate(-1)

print(data[0])
end_time = int(round(time.time() * 1000))
print('실행 시간 : %d(ms)' % (end_time - start_time))