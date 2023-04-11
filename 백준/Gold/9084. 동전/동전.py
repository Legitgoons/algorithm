import sys
input = lambda : sys.stdin.readline()
t = int(input())

for _ in range(t) :
    # n = 동전의 종류, k = 목표값
    n = int(input())
    coin = list(map(int, input().split())) # 동전을 저장할 배열
    k = int(input())

    dp = [0 for _ in range(k+1)]
    dp[0] = 1 # dp[0] = 0 일 경우 dp[1] = 0이 되어버리기 때문에 dp[0] = 1 로 설정

    for c in coin: #동전의 종류대로 순회 (예제의 경우 1, 2, 5)
        for i in range(c, k+1): #1부터 10까지, 2부터 10까지, 5부터 10까지 순회
            dp[i] += dp[i-c] #경우의 수 쌓아감

    print(dp[k]) #목표값이 달성된 경우의 수 출력