import sys
input = lambda : sys.stdin.readline()
from bisect import bisect_left #이진탐색 라이브러리 import

trs = input() #그냥 버림
arr = list(map(int, input().split()))
dp = []

for i in arr: #배열 순회
    x = bisect_left(dp, i) #i가 들어갈 위치 x
    if len(dp) <= x: # x가 배열의 길이보다 크다면 = i가 가장 큰 수라면
        dp.append(i) # i를 배열에 추가
    else:
        dp[x] = i #자신보다 큰 수 중 가장 작은수와 교체
print(len(dp))