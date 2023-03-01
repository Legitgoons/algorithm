arr = []
breaker = False
for i in range(9) :
    arr.append(int(input()))

arr.sort()

key = sum(arr) - 100
for i in arr :
    for j in arr :
        if i != j and i+j == key :
            arr.remove(i)
            arr.remove(j)
            breaker = True
            break
    if breaker == True :
        break

for i in arr :
    print(i)