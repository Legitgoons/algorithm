y, x = map(int, input().split())
yList = [0, y]
xList = [0, x]
n = int(input())

#가로/세로 리스트 만들고 거기다 정렬 -> 뒤에 값에서 앞에 값 빼주기 -> 곱해서 그 중 최대값 출력
for _ in range(n) :
    gase, num  = map(int, input().split())
    if gase == 0 :
        xList.append(num) 
        xList.sort()
    elif gase == 1 :
        yList.append(num)
        yList.sort()
mx = 0
for n in range(len(xList)-1) :
    for m in range(len(yList)-1) :
        if mx < (xList[n+1]-xList[n])*(yList[m+1]-yList[m]) :
            mx = (xList[n+1]-xList[n])*(yList[m+1]-yList[m])
print(mx)