import sys
from collections import deque
input = lambda : sys.stdin.readline()

N, M = map(int, input().split()) #N은 기차의 수, M은 명령의 수
deq = [deque(0 for _ in range(20))for i in range(N)] #한칸씩 앞뒤로 이동시키기엔 deque.rotate가 최고
ans = [] #check용 배열

for i in range(M):
    arr = list(map(int, input().split())) #몇개인지 모르니까 일단 list에 넣자
    if arr[0] == 1 :
        deq[arr[1]-1][arr[2]-1] = 1 #i번째 기차의 x번째 좌석 = 1
    elif arr[0] == 2 :
        deq[arr[1]-1][arr[2]-1] = 0 #i번째 기차의 x번째 좌석 = 0
    elif arr[0] == 3 :
        deq[arr[1]-1].rotate(1) #뒤로 이동
        deq[arr[1]-1][0] = 0 #맨 앞칸은 0
    elif arr[0] == 4 :
        deq[arr[1]-1].rotate(-1) #앞으로 이동
        deq[arr[1]-1][19] = 0 #맨 뒷칸은 0
for i in deq:
    if i not in ans :
        ans.append(i)
print(len(ans))
#기차는 20개의 일렬 좌석
#1 -> 사람 태우기
#2 -> 사람 내리기
#3 -> 한칸씩 뒤로 가기, 20번째 칸이면 하차
#4 -> 한칸씩 앞으로 가기, 1번째 칸이면 하차
# 항상 이런 문제면 포인터 움직여서 하려다가 실패함. 이번엔 rotate로 움직이자
# 1, 2, 3, 4 각각에 따라 함수 정해놓고 실행시키자 -> 걍 조건문으로 바로 돌리자 귀찮당