n = int(input())
for i in range(0, n): 
        for m in range(0, i) :
            print(" ", end="")
        for j in range(n-i, 0, -1) :
            print("*", end="")
        print("")