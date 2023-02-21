n = int(input())
for i in range(0, n) :
    for j in range(0, i) :
        print(" ", end='')
    if i == 0 :
        for j in range(0, n) :
            print("*", end='')
        for j in range(0, (2*(n-1))-1): #gap 출력
            print(" ", end='')
        for j in range(0, n) :
            print("*", end='')
    elif i==n-1:
        for j in range(0, (2*n)-1):
            if j == 0 or j == n-1 or j == (2*n)-2 :
                print("*", end='')
            else : 
                print(" ", end='')      
    else :
        for j in range(0, n): 
            if j == 0 or j == n-1 :
                print("*", end='')
            else : 
                print(" ", end='')    
        for j in range(0, (2*(n-i))-3): #gap 출력
            print(" ", end='')
        for j in range(0, n):
            if j == 0 or j == n-1 :
                print("*", end='')
            else : 
                print(" ", end='')
    print("")

for i in range(1, n) :
    for j in range(0, n-i-1) :
        print(" ", end='')
    if i == n-1 :
        for j in range(0, n) :
            print("*", end='')
        for j in range(0, (2*(n-1))-1): #gap 출력
            print(" ", end='')
        for j in range(0, n) :
            print("*", end='')   
    else :
        for j in range(0, n): 
            if j == 0 or j == n-1 :
                print("*", end='')
            else : 
                print(" ", end='')    
        for j in range(0, (2*i)-1): #gap 출력
            print(" ", end='')
        for j in range(0, n):
            if j == 0 or j == n-1 :
                print("*", end='')
            else : 
                print(" ", end='')
    print("")