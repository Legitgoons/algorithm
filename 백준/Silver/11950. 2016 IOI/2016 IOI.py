N, M = map(int, input().split())
flag = [list((input())) for _ in range(N)] #파이썬은 문자열 굳이 안쪼개도 알아서 쪼개서 받음

mn = M*N

wCnt = 0

for w in range(0,N-2): # 밑에 2줄은 있어야 해
    for k in range(M):
        if flag[w][k] != 'W':
            wCnt += 1

    bCnt = 0
    for b in range(w+1,N-1): # 위에 1줄, 밑에 1줄은 있어야 해
        for k in range(M):
            if flag[b][k] != 'B':
                bCnt += 1

        rCnt = 0
        for r in range(b+1,N): 
            for k in range(M):
                if flag[r][k] != 'R':
                    rCnt += 1

        cnt = wCnt+bCnt+rCnt
        mn = min(mn, cnt)
print(mn)