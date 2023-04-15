import sys
input = lambda : sys.stdin.readline()

arr = []
add = 0
for i in range(5):
    arr.append(int(input()))
    add += arr[i]

arr.sort()
print(add//5)
print(arr[2])