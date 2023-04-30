import sys
input = lambda : sys.stdin.readline()
sys.setrecursionlimit(10**6) #무한 탐색 방지


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) #여기까지 입력

visited = [0 for _ in range(n+1)] #방문처리

arr = []

def dfs(x):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = x
            dfs(i)
dfs(1)

for i in range(2, n+1):
    print(visited[i])