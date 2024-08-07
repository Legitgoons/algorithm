import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
left, right = 0, 1
cnt = 0

while right<=N and left<=right:
    add = num[left:right]
    total = sum(add)
    if total == M:
        cnt += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1
        
print(cnt)