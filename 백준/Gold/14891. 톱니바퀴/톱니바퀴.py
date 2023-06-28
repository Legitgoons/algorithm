import sys
input = lambda : sys.stdin.readline()
from collections import deque


def rotationRight(num):
    wheel[num].appendleft(wheel[num].pop())


def rotationLeft(num):
    wheel[num].append(wheel[num].popleft())


def rotateWheel(start, direction):
    gears_to_rotate = set()
    gears_to_rotate.add(start)

    left_num = start - 1
    left_direction = direction

    while left_num >= 0:
        if wheel[left_num][2] != wheel[left_num + 1][6]:
            gears_to_rotate.add(left_num)
            left_direction = -left_direction
        else:
            break
        left_num -= 1
    right_num = start + 1
    right_direction = direction

    while right_num < 4:
        if wheel[right_num - 1][2] != wheel[right_num][6]:
            gears_to_rotate.add(right_num)
            right_direction = -right_direction
        else:
            break
        right_num += 1

    for gear in gears_to_rotate:
        if gear % 2 == start % 2:
            if direction == 1:
                rotationRight(gear)
            else:
                rotationLeft(gear)
        else:
            if direction == 1:
                rotationLeft(gear)
            else:
                rotationRight(gear)

wheel = [deque() for _ in range(4)]
for i in range(4):
    wheel[i] = deque(map(int, input().strip()))

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    rotateWheel(a - 1, b)

cnt = 0
for i in range(4):
    if wheel[i][0] == 1:
        cnt += 2 ** i

print(cnt)
