from collections import deque
import sys
read = lambda : sys.stdin.readline()

N, M = map(int, read().split())
target = list(map(int, read().split()))

deq = deque()
for i in range(1, N+1) :
    deq.append(i)

count = 0 #2, 3번 실행 기록용 변수
check = 0 #출력횟수 기록용 변수

for i in target :
    while(check != M) :
        if i == deq[0] :
            deq.popleft()
            check += 1
            break
        elif deq.index(i) < len(deq)/2 :
            while deq[0] != i :
                deq.append(deq.popleft())
                count+=1
        else :
            while deq[0] != i :
                deq.appendleft(deq.pop())
                count+=1

print(count)
