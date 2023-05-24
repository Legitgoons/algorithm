import sys
input = lambda : sys.stdin.readline()

x, y = input().split() #걍 문자열로 입력받음
x = int(x[::-1])
y = int(y[::-1])

if x > y:
    print(x)
else :
    print(y)