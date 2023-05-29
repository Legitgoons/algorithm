import sys
input = lambda : sys.stdin.readline()
N, K = map(int, input().split())
num = K*(K+1) // 2

if N < num:
    print(-1)
elif (N - num) % K == 0:
    print(K-1)
else:
    print(K)