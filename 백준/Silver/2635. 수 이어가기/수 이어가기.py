N = int(input())
max = 0
index = 0

for i in range(1, N+1) :
    x = N
    l = i
    cnt = 0
    while(True) :
        if 0 <= x-l :
            temp = x
            x = l
            l = temp-l
            cnt+=1
        else :
            break
    if max < cnt :
        index = i
        max = cnt

arr = [N, index]
x = N
l = index
while(True) :
    if 0 <= x - l:
        temp = x
        x = l
        l = temp - l
        arr.append(l)
    else:
        break

print(len(arr))
for i in arr :
    print(i, end=" ")
print()
# max받았을때 i값 저장 + max값 저장
# 결과 나오면 minus 한번 더 써서 식 출력