import sys
read = lambda : sys.stdin.readline().rstrip()

n = int(read())
word = list(set(str(read()) for _ in range(n)))
word.sort() 
word.sort(key = lambda x: len(x)) 

for i in word:
    print(i)