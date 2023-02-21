n = int(input())
for i in range(1, n+1): 
        for m in range(n-i, 0, -1) :
            print(" ", end="")
        for j in range(0, i) :
            print("*", end="")
        print("")