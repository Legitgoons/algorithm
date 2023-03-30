import sys
input = lambda : sys.stdin.readline()

N = int(input())
arr = list(map(int, input().split())) #입력
dp = [0 for i in range(N)] #합계 셀 list
for i in range(N):
    dp[i] = arr[i] #일단 자신의 값을 다 넣어줌

# mx = 0
for i in range(N) :
    for j in range(i) :
        if arr[i] < arr[j] and dp[i] < arr[i] + dp[j]: # 현재 위치의 원소가 이전 위치의 원소보다 작고, 현재 저장된 값보다 이전값+현재원소의 합이 크면
            dp[i] = arr[i] + dp[j] # 현재원소값 + 이전 값까지의 합계를 dp[i]에 넣어줌
print(max(dp)) #dp 배열 중 최대값과 mx값 비교