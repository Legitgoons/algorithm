day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = 0

a, b = map(int, input().split())
for i in range(0, a-1) :
    answer += month[i]
print(day[(answer+b)%7])