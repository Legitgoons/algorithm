from collections import deque
import sys
input = sys.stdin.readline()

def solution(skill, skill_trees):
    answer = 0
    
    for arr in skill_trees : #한 문단씩 분리
        flag = False #반복문 탈출용 
        skilldeq = deque(skill) #덱에 넣자
        for i in arr : #문단에서 한 글자씩 분리
            if i in skill : #글자가 스킬에 있다면
                if i == skilldeq.popleft() : #덱에서 맨 앞에 있는 스킬인지 확인
                    continue
                else :
                    flag = True
                    break
        if flag == False : answer+=1
            
    return answer

print('CBD', 'BACDE', 'CBADF', 'AECB', 'BDA')