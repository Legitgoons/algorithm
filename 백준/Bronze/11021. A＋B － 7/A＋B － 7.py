T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
for i in range(0, T) :
    print(f'Case #{i+1}: {arr[i][0]+arr[i][1]}')