import sys
read = lambda: sys.stdin.readline()

N = int(input())
A = set(map(int, read().split()))
M = int(input())
B = list(map(int, read().split()))

for i in B : 
    if i in A :
        print(1)
    else :
        print(0)