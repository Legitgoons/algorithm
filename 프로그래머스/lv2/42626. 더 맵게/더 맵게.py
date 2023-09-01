import sys, heapq
input = sys.stdin.readline

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #scoville을 최소힙으로 만듬
    
    while scoville[0] < K : #최소값이 K값 이상이 될때까지
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        
        if len(scoville) < 2 and scoville[0] < K : #추가적인 제한사항 구현
            return -1

    return answer