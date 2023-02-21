T = int(input())
for i in range(0, T) :
    a,b = map(int,input().split(','))
    if 0<a and b<10 :
        print(a+b)