from collections import deque

T = int(input())
que = deque()

for i in range (1, T+1) :
    que.append(i)
for i in range(0, T-1) :
    que.popleft()
    que.append(que.popleft())

print(que.popleft())