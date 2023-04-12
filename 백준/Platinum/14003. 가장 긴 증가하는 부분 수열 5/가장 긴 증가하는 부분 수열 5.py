import sys
input = lambda : sys.stdin.readline()
from bisect import bisect_left #이진탐색 라이브러리 import

N = int(input())
arr = list(map(int, input().split())) # 여기까지 입력
ans = [arr[0]] # 정답 list(첫 번째 숫자 넣어줌)
value = [[0,0] for _ in range(N)] # value list (0, 0 으로 초기화)

value[0][1] = arr[0] 
for i in range(1, N) : # 1부터 N까지 반복
    value[i][1] = arr[i] # value 배열 2번째 칸을 모두 arr배열의 값으로 채워줌

    if ans[-1] < arr[i] : # 마지막 값보다 arr배열의 i번째 값이 더 크다면 (= i번째 값이 가장 큰 수라면)
        value[i][0] = len(ans) # value 배열의 첫번째 값에 현재 ans배열의 길이 입력
        ans.append(arr[i]) # ans 배열에 arr배열의 i번째 값 추가

    else : # 마지막 값보다 i번째 값이 작거나 같다면( = i가 가장 큰 수가 아니라면)
        idx = bisect_left(ans, arr[i]) # ans배열에 i번째 숫자가 들어갈 위치 찾아줌
        ans[idx] = arr[i]  # 찾았으니까 넣어주자
        value[i][0] = idx  # value배열의 i번째 칸의 첫번째 값에 위치값 넣어주기
    #여기까지 list 채우기

#이제 진짜 정답 list를 찾아보자
idx = len(ans) - 1 # ans길이에서 1을 빼줘서 idx가 ans의 마지막 숫자를 포인팅하도록 변경
answer = [] # 정답 list(ㄹㅇ)
for i in range(N-1, -1, -1) : # 배열의 길이-1해줘서 끝에서 마지막 값부터 찾도록
    if idx < 0: # 혹시 0보다 작아지면 끝!
        break

    if idx == value[i][0] : # value배열의 첫번째 자리 값과 idx값이 같다면
        answer.append(value[i][1]) # value배열의 두번째 자리 값(숫자값)을 정답 list(ㄹㅇ)에 추가
        idx -= 1 # 찾았으니까 idx값에서 1을 빼서 다음 값을 찾으러 감

print(len(answer))
for i in range(len(answer)-1, -1, -1) :
    print(answer[i], end=" ")