from collections import deque #큐 대신 덱 사용
import sys
input = lambda : sys.stdin.readline()

N, M, V = map(int, input().split())
line = [[0 for i in range(N+1)] for _ in range(N+1)] # 인접 행렬 선언
visit1 = [0 for i in range(N+1)] # DFS방문처리 list
visit2 = [0 for i in range(N+1)] # BFS방문처리 list
deq = deque()
for i in range(M) :
    x, y = map(int, input().split())
    line[x][y] = 1 # 인접하는 배열 표시해줌
    line[y][x] = 1

def dfs(v):
    visit1[v] = 1 #방문처리
    print(v, end = ' ')
    for i in range(1, N+1) :
        if line[v][i] == 1 and visit1[i] == 0 : #인접한 배열에 아직 방문하지 않았다면
            dfs(i) #재귀함수로 방문

def bfs(v):
    deq.append(v) #덱에 탐색할 노드를 먼저 넣어줌
    visit2[v] = 1 # 방문처리
    while deq : #덱에 값이 남아있을때까지 반복
        v = deq.popleft() #맨 앞에 있는 값 pop
        print(v, end=' ') #해서 출력해줌
        for i in range(1, N+1):
            if line[v][i] == 1 and visit2[i] == 0 : #방문한 노드에 인접한 노드에 아직 방문하지 않았다면
                deq.append(i) #덱에 i값을 넣어줌
                visit2[i] = 1 #방문처리

dfs(V)
print()
bfs(V)