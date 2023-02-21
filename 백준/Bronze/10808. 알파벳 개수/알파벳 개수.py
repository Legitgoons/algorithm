n = input()
arr = [0]*26 


for i in n:
    arr[ord(i)-97] += 1
    
for i in arr:
    print(i, end=' ')