import sys
input = lambda : sys.stdin.readline()

N, K = map(int, input().split()) # N = 총 날짜, K = 더할 날짜

arr = list(map(int,input().split()))
ondo = sum(arr[0:K]) # 첫날부터 K일까지 슬라이딩
max = ondo
for i in range(N-K) : #첫번째 날은 위에서 계산했으니까 두번째 날부터 마지막날까지 계산
    #1 ~ N-K+1이여서 0 ~ N-K+1로 수정
    ondo = ondo-arr[i]+arr[K+i] #더해준 날 중 첫번째 날을 빼고 맨 뒤에 날을 더해줌
    if max < ondo :
        max = ondo


print(max)