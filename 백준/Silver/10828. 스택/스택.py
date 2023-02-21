import sys

t = int(input())
stact = []
for i in range(0, t) :
    command = sys.stdin.readline().split()
    if command[0] == 'push' :
        stact.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stact) == 0 :
            print(-1)
        else :
            print(stact.pop())
            # stact.pop()
    elif command[0] == 'size':
        print(len(stact))
    elif command[0] == 'empty':
        if len(stact) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == 'top':
        if len(stact) == 0 :
            print(-1)
        else :
            print(stact[-1])