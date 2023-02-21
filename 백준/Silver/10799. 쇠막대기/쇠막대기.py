from collections import deque
import sys
read = lambda : sys.stdin.readline().strip()

arr = list(read())
ans = 0
dq = deque()

for i in range(len(arr)):
    if arr[i] == '(':
        dq.append('(')
    else:
        if arr[i-1] == '(': 
            dq.pop()
            ans += len(dq)
        else:
            dq.pop() 
            ans += 1 

print(ans)