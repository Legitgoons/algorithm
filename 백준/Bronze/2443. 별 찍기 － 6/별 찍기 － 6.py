a = int(input())
for i in range(0, a) :
    for k in range(0, i) :
        print(" ", end='')
    for j in range(0, (2*a)-1-2*i) :
        print("*", end='')
    print("")