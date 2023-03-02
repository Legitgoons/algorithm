N = int(input())
if N%5==0 :
    print(N//5)
elif N%5==3 :
    print((N//5)+1)
elif (N-6)%5==0 and 0<=N-6:
    print((N//5)-1+2)
elif (N-9)%5==0 and 0<=N-9:
    print((N//5)-1+3)
elif (N-12)%5==0 and 0<=N-12:
    print((N//5)-2+4)
else :
    print(-1)


#5로 나누고 나머지 3으로
# 3 6 9 12까지는 ok
#나머지 3으로 나눔