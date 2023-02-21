import sys

t = int(input())
stact = []
sum = 0
for i in range(0, t) :
    a = int(input())
    if a == 0 :
        stact.pop()
    else :
        stact.append(a)

for i in range(0, len(stact)) :
    sum += stact[i]

print(sum)