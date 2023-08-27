import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0] * 7 for _ in range(3)]
for i in range(N) :
    x, y = map(int, input().split())
    arr[x][y] += 1
#여기까지 입력

cnt = 0

for i in arr :
    for j in i :
        cnt += math.ceil(j/K)
print(cnt)
