from collections import deque
import sys
read = lambda : sys.stdin.readline()

T = int(read())

for _ in range (0, T) :
    flag = 0
    command = list(read().replace('\n', ''))
    trash = int(read())
    arr = map(int, read().replace('[', '').replace(',', ' ').replace(']\n', '').split())
    dq=deque(arr)

    for i in command :
        if i == 'R' :
            flag = 1 - flag
        elif i == 'D' :
            if len(dq) == 0 :
                print("error")
                break
            else :
                if flag == 0:
                    dq.popleft()
                else:
                    dq.pop()
    else : 
        if flag == 1:
            dq.reverse()
        print('[' + ','.join([str(val) for val in dq]) + ']')