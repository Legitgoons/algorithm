import sys
from collections import deque
read = lambda : sys.stdin.readline()

N, K = list(map(int, input().split()))
deq = deque()

for i in range(1, N+1) :
    deq.append(i)

print("<", end='')
while len(deq) != 1 :
    for i in range(K-1) :
        deq.append(deq.popleft())
    print(deq.popleft(),end='')
    print(', ',end='')

print(deq.pop(),end='')
print('>')