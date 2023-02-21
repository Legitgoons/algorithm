from sys import stdin
input = stdin.readline

N, M, q = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
query = [list(map(int,input().split())) for _ in range(q)]

for qNum in range(0, q) : #query number check
    i = query[qNum][1]
    j = query[qNum][2]
    swap = 0
    if query[qNum][0] == 0 :
        arr[i][j] = query[qNum][3] 
    else :
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

for a in range(0, N) :
    print(*arr[a])