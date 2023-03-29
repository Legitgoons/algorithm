from collections import deque #큐 대신 덱 사용
import sys
input = lambda : sys.stdin.readline()

n = int(input())
m = int(input())
visited = [0 for _ in range(n+1)]
line = [[0 for _ in range(n+1)] for i in range(n+1)] #인접 행렬
deq = deque() # 덱 선언
cnt = 0
for i in range(m):
    x, y = map(int, input().split())
    line[x][y] = line[y][x] = 1 #인접 행렬 연결

def bfs(node) :
    deq.append(node) #덱에 시작node 넣어줌
    global cnt
    visited[node] = 1 #방문처리
    while deq : #덱이 빌때까지
        v = deq.popleft() # 덱의 맨 앞에 있는 수를 v에 넣음
        cnt += 1
        for i in range(1, n+1) :
            if(visited[i] == 0 and line[v][i] == 1) : #현재 노드값에 연결된 노드 중 방문하지 않은 노드가 있을때
                deq.append(i)
                visited[i] = 1 #방문처리

bfs(1)
print(cnt-1) #1번 컴퓨터는 제외