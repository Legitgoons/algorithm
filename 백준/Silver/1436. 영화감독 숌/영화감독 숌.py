import sys
input = lambda :sys.stdin.readline()

n = int(input())
sixCnt = 0
cnt = 666

while True:
    if '666' in str(cnt):
        sixCnt += 1
        if sixCnt == n:
            print(cnt)
            break
    cnt += 1