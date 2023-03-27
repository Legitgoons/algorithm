tc = int(input())

for i in range(tc):
    n = int(input())
    dp  = [0 for i in range(n+1)] #0~n까지의 리스트 만들기
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[i])