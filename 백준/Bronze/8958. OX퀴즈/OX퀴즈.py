n=int(input())
for i in range(0,n):
    count=0
    c = 1
    arr=list(input())
    for j in arr:
        if j=='O':
            count+=c
            c+=1
        else:
            c=1
    print(count)