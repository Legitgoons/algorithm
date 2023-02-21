arr1 = 26*[0]
arr2 = 26*[0]
answer = 0

for i in list(input()):
    arr1[ord(i) - 97] += 1
for i in list(input()):
    arr2[ord(i) - 97] += 1

for i in range(26):
    answer += abs(arr1[i]-arr2[i])
print(answer)