from collections import deque
import sys
read = lambda : sys.stdin.readline()

dq = deque()

sum = 1
ans = 0
bracket = list(read().replace('\n', ''))


for i in range(len(bracket)) :
    
    if bracket[i] == '('  :
        dq.append(bracket[i])
        sum *= 2

    elif bracket[i] == '[':
        dq.append(bracket[i])
        sum *= 3


    elif bracket[i] == ')' :
        if len(dq) == 0 or dq[-1] == '[' :
            ans = 0
            break
        elif bracket[i-1] == '(' :
            ans += sum
        dq.pop()
        sum//=2

    else :
        if len(dq) == 0 or dq[-1] == '(' :
            ans = 0
            break
        elif bracket[i-1] == '[' :
            ans += sum
        dq .pop()
        sum//=3

if len(dq) != 0 :
    print(0)
else :
    print(ans)