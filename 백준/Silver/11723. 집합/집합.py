import sys
input = lambda : sys.stdin.readline().rstrip()

s = set() #집합 선언
M = int(input())
for _ in range(M) :
    command = list(input().split())
    if command[0] == "add" :
        s.add(int(command[1]))
    elif command[0] == "remove" :
        if(int(command[1]) in s) :
            s.remove(int(command[1]))
    elif command[0] == "check":
        if(int(command[1]) in s) :
            print(1)
        else :
            print(0)
    elif command[0] == "toggle":
        if(int(command[1]) in s) :
            s.remove(int(command[1]))
        else :
            s.add(int(command[1]))
    elif command[0] == "all":
        s.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif command[0] == "empty":
        s.clear()