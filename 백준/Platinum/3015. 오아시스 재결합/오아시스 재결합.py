import sys
input = lambda : sys.stdin.readline()
from collections import deque

deq = deque()
cnt = 0

N = int(input())
for _ in range(N) :
    x = int(input())

    if len(deq) != 0 : #덱이 0이 아니라면

        if x < deq[-1][0]: #마지막사람보다 작으면 그냥 추가
            deq.append([x, 1])

        elif x == deq[-1][0]: # 만약에 마지막사람이랑 같으면
            deq.append([x, deq.pop()[1] + 1]) # 마지막값의 크기에 1을 추가해서 돌려줌

        else : #덱의 마지막값보다 큰 값이 들어오면
            while deq and deq[-1][0] < x : #덱에 남은 값이 있고 새 값이 덱의 마지막값보다 클때까지
                if len(deq) != 1 : #지금 있는 값이 deque의 마지막 값이 아니라면
                    cnt += deq[-1][1]
                for i in range(1, deq[-1][1]) : #N-1+...+1
                    cnt += i
                cnt+=deq[-1][1] #x랑 마지막값의 쌍
                deq.pop()  # pop

            if deq and x == deq[-1][0]:  # 만약에 마지막값이랑 같으면
                deq.append([x, deq.pop()[1] + 1])  # 마지막값의 크기에 1을 추가해서 돌려줌
            else :
                deq.append([x, 1])
    else :
        deq.append([x, 1]) #현재 덱이 비었으면 그냥 추가

while deq :  #마지막 체크(덱에 남은 값이 없을때까지)
    if len(deq) != 1:  # 지금 있는 값이 deque의 마지막 값이 아니라면
        cnt += deq[-1][1] # cnt += N
    for i in range(1, deq[-1][1]):  # N-1+...+1
        cnt += i
    deq.pop()  # pop

print(cnt)

# [숫자][개수]
# N+N-1+...+1