import sys
input = lambda : sys.stdin.readline()

n = int(input())
dp = [[0, []] for _ in range(n+1)] #배열 생성
dp[1][0] = 0 #값
dp[1][1] = [1] #경로

for i in range(2, n + 1): #1은 뛰어넘고 2부터 시작

    dp[i][0] = dp[i - 1][0] + 1 #1을 뺀 값의 계산횟수 + 1
    dp[i][1] = dp[i - 1][1] + [i]
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]: #1을 뺀 값보다 3으로 나눈 값의 횟수가 작다면
        dp[i][0] = dp[i // 3][0] + 1 # 3으로 나눈 값의 횟수 넣기
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]: #지금까지의 값보다 2로 나눈 값의 횟수가 작다면
        dp[i][0] = dp[i // 2][0] + 1 #값에 2로 나눈 값의 횟수 넣기
        dp[i][1] = dp[i // 2][1] + [i]
        
print(dp[n][0]) #값 출력
print(*reversed(dp[n][1])) #경로 출력