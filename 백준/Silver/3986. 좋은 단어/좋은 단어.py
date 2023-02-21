import sys

t = int(input())
answer = 0
for _ in range(0, t) :
    line = input()
    stact = []
    for i in line :
        if len(stact) == 0 :
            stact.append(i)
        else :
            if stact[-1] == i :
                stact.pop()
            else :
                stact.append(i)
    if len(stact) == 0 :
        answer += 1

print(answer)