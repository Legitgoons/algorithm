import sys
from collections import deque
input = sys.stdin.readline

deq = deque() # 대기차량 담을 deque
N, M = map(int, input().split()) #주차공간 N개, 차량 M대
pay = [] #가격 담을 list
weight = [] #무게 담을 list
cnt = 0 #답

check = [0 for _ in range(N)] #주차공간 사용중인지 check할 리스트
for _ in range(N):
    pay.append(int(input()))
for _ in range(M) :
    weight.append(int(input()))
for _ in range(2*M) :
    x = int(input())
    if 0 < x : #새로 입력받은게 양수라면
        if 0 in check : # 빈 자리 있는지 확인하고
            for i in range(N) :
                if check[i] == 0 :
                    check[i] = x #넣어줌
                    break
        else : deq.append(x) #빈 자리 없으면 대기석으로
    else : #입력받은게 음수면
        if abs(x) in check: #지금 주차중이면
            for i in range(N) :
                if check[i]+x == 0 :
                    cnt += weight[check[i]-1]*pay[i] #찾아서 cnt에 더해주고
                    if deq : #대기 리스트 확인
                        check[i] = deq.popleft() #있으면 넣어주기
                    else : check[i] = 0  #자리 비워주기
                    break
print(cnt)