from collections import deque
import sys
read = lambda : sys.stdin.readline()

t = int(read())

for i in range(0, t):
    n, m = map(int, read().split())
    deq = deque(list(map(int, read().split())))
    cnt = 0
    while deq:
        best = max(deq)  
        front = deq.popleft() 
        m -= 1

        if best == front : 
            cnt += 1 
            if m < 0 : 
                print(cnt)
                break
        else :   
            deq.append(front)
            if m < 0 :  
                m = len(deq) - 1 