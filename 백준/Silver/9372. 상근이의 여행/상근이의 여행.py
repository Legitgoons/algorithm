import sys
read = lambda: sys.stdin.readline()

t = int(read())

for _ in range(t):
    n, m = map(int, input().split())
    for i in range(m):
        read() 
    print(n - 1)