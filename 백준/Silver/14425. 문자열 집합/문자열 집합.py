import sys
input = sys.stdin.readline

dic = {}
cnt = 0
N, M = map(int, input().split())

for _ in range(N):
    word = input().rstrip()
    dic[word] = True

for _ in range(M):
    word = input().rstrip()
    if word in dic:
        cnt += 1

print(cnt)