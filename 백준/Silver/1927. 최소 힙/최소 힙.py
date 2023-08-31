import sys
import heapq
input = lambda: sys.stdin.readline()

heap = []

for i in range(int(input())):
    n = int(input())
    if n == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)