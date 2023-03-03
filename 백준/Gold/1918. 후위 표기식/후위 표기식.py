import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()
deq = deque() # 연산자가 들어갈 덱
arr = list((read())) # 나눠서 입력받음
cal = list() # 답

def Comparison(i) :
    if (i == '*' or i == '/') :
        return 2
    elif(i == '+' or i == '-') :
        return 1
    else :
        return 0; # 여는 괄호는 가장 낮은 값 반환

for i in arr :
    if 'A' <= i and i <= 'Z' : # 알파벳이면
        cal.append(i) # 답 리스트에 넣어줌
    else : # 아니면
        if i == '(': # 여는괄호는 
            deq.append(i) # 덱에 넣어줌
        elif i == ')' : # 닫는괄호를 만나면
            while(deq and deq[-1] != '(') : # 덱이 비거나 여는 괄호를 만날 때까지
                cal.append(deq.pop()) # 덱에서 꺼내서 답에 넣어줌
            if(deq) : # 덱이 비어서 종료된게 아니라면
                deq.pop() # 여는 괄호를 pop
        else : # 연산자라면
            while(deq and Comparison(i) <= Comparison(deq[-1])) :
                cal.append(deq.pop()) #덱에서 pop해서 문자열에 넣어줌
            deq.append(i) # 다 꺼냈으면 덱에 push
while(deq) :
    cal.append(deq.pop())

for i in cal :
    print(i, end='')