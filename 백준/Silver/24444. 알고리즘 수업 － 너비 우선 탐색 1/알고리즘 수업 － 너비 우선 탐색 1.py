from collections import deque #큐 대신 덱 사용
import sys
input = lambda : sys.stdin.readline()

N, M, V = map(int, input().split())
line = [[] for _ in range(N+1)] # 인접 행렬 선언
visit = [0 for i in range(N+1)] # BFS방문처리 list
cnt = 1
for i in range(M) :
    x, y = map(int, input().split())
    line[x].append(y) # 인접하는 배열 표시해줌
    line[y].append(x)

def bfs(v):
    global cnt
    deq = deque()

    deq.append(v) #덱에 탐색할 노드를 먼저 넣어줌
    visit[v] = 1 # 방문처리
    while deq : #덱에 값이 남아있을때까지 반복
        v = deq.popleft() #맨 앞에 있는 값 pop
        line[v].sort() #오름차순 정렬
        for i in line[v]:
            if visit[i] == 0 : #방문한 노드에 인접한 노드에 아직 방문하지 않았다면
                cnt += 1
                visit[i] = cnt #방문처리
                deq.append(i) #덱에 i값을 넣어줌

bfs(V)
for i in range(1, N+1):
    print(visit[i])