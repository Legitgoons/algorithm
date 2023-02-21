import math

number = input()
target = list(map(int, str(number)))
count = [0 for i in range(10)]
set = 1

for i in range(0, 10) :
    for j in range(0, len(target)) :
        if i == target[j] :
            count[i] += 1

six9ine = count[6]+count[9]
if set < math.ceil(six9ine/2): #round는 짝수방향으로 반올림처리하기에 올림인 math.ceil 사용
    set = math.ceil(six9ine/2)
count[6] = 0
count[9] = 0

for i in range(0, 10):
    if set<count[i]:
        set=count[i]
        
print(set)