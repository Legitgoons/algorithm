a = int(input())
b = int(input())
c = int(input())

arr = str(a * b * c)

for num in range(10):
    count = arr.count(str(num))
    print(count)