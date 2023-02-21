a = int(input())
for i in range(0, a-1) :
    for k in range(a-i-1, 0, -1) :
        print(" ", end='')
    for j in range(0, 1+(2*i)):
        print("*", end='')
    print("")
for i in range(0, a) :
    for k in range(0, i) :
        print(" ", end='')
    for j in range(0, (2*a)-1-2*i) :
        print("*", end='')
    print("")
