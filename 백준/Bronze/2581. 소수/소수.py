import sys
input = lambda :sys.stdin.readline()

M = int(input())
N = int(input())

cnt = 0
mn = 10000
for i in range(M, N+1) : #M이상 N이하
    for j in range(2, i+1) : #2부터 i값까지 순회
        if i % j == 0 : #나누어 떨어지는데
            if i == j : #자기랑 만나서 나누어 떨어지는거면
                cnt+=i
                mn = min(mn, i)
            break
if cnt == 0:
    print(-1)
else :
    print(cnt)
    print(mn)