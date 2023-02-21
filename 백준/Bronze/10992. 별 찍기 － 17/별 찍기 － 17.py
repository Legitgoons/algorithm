n = int(input())
for i in range(1, n+1) :
    for j in range(n-i, 0, -1):
        print(" ", end='')
    for j in range(0, i*2-1):
        if i == n :
            print("*", end="")
        elif j == 0 or j == i*2-2 :
            print("*", end="")
        else :
            print(" ", end="")
    print("")