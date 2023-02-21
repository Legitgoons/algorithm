n = int(input())
arr = list(map(int, input().split()))
ans = int(input())
count = 0

for i in range (0, len(arr)) :
    if arr[i] == ans :
        count += 1
print(count)