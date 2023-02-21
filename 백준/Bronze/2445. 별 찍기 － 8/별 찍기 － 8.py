n = int(input())
for i in range(1, n+1) :
    for j in range(0, i) :
        print("*", end="")
    for j in range(0, (2*n)-2*i) :
        print(" ", end='')
    for j in range(0, i) :
        print("*", end="")
    print("")
for i in range(1, n) :
    for j in range(n-i, 0, -1) :
        print("*", end="")
    for j in range(0, i*2) :
        print(" ", end='')
    for j in range(n-i, 0, -1) :
        print("*", end="")
    print("")