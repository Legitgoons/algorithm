t = int(input())
for i in range(0, t):
    r, s = input().split()
    text = ''
    for i in s:
        text += int(r) * i
    print(text)