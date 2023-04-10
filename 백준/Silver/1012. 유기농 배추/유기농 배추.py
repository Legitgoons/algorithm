import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs(y, x):
    que = deque() #덱 선언(큐 대신)
    que.append((y, x)) #큐에 y, x값 넣어줌
    while que: #큐가 남아 있는 동안
        y, x = que.popleft() #큐에서 꺼내서
        for i in range(4): #4방향 탐색
            ny = y + dy[i] #델타
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and baechu[ny][nx] == 1: #델타값이 map을 넘어가지 않고 길이 있다면
                que.append((ny, nx)) #그 값을 큐에 넣어주고
                baechu[ny][nx] = 2 #다시 순회하지 않도록 값을 2로 수정
    return 1


dy = [-1, 1, 0, 0] #델타순회
dx = [0, 0, -1, 1]

T = int(input())
for t in range(T) :
    M, N, K = list(map(int,input().split()))
    baechu = [[0 for _ in range(N)] for i in range(M)]

    for _ in range(K):
        y, x = map(int, input().split())
        baechu[y][x] = 1 # 배추 위치 표시

    cnt = 0
    for i in range(M) :
        for j in range(N) :
            if baechu[i][j] == 1:
                cnt += bfs(i, j)
    print(cnt)