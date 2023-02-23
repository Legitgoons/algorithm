import sys
read = lambda: sys.stdin.readline()

N = int(input())
A = sorted(list(map(int, read().split()))) 
M = int(input())
B = list(map(int, read().split()))

dict = {} #빈 중괄호 == dict 선언 or f = dict()로도 선언 가능

for i in A : # A순회
    if i in dict : # i라는 key값을 가진 항목이 dict에 있다면
        dict[i] += 1 # value값에 1을 추가해줌
    else : # 없다면
        dict[i] = 1 # dict에 key값은 i value값은 1인 항목을 추가해줌

for i in B : #B 순회
    if i in dict : # i라는 key값을 가진 항목이 dict에 있다면
        print(dict[i], end=' ') # 그 항목이 가진 value값 출력
    else : #없다면
        print(0, end=' ') #0