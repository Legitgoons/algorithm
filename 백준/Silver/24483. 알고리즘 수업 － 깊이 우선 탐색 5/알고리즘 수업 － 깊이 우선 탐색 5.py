import sys
input = lambda : sys.stdin.readline()
sys.setrecursionlimit(10**6) #재귀 깊이 에러 방지

N, M, V = map(int, input().split())
line = [[] for _ in range(N+1)] # 인접 행렬 선언
visit = [[-1, 0] for i in range(N+1)] # DFS방문처리 list
cnt = 1

for _ in range(M) :
    x, y = map(int, input().split())
    line[x].append(y) # 인접하는 배열 표시해줌
    line[y].append(x)

def dfs(v):
    global cnt
    line[v].sort() # 정점 번호를 오름차순으로 방문
    for i in line[v]:
        if visit[i][0] == -1: #인접한 배열에 아직 방문하지 않았다면
            cnt += 1
            visit[i] = [visit[v][0]+1, cnt]
            dfs(i) #재귀함수로 방문, 깊이 + 1
visit[V][0] = 0
dfs(V)
ans = 0
for i in range(1, N+1):
    ans += visit[i][0]*visit[i][1]
print(ans)