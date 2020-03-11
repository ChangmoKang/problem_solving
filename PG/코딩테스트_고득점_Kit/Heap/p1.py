import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        
        heapq.heappush(scoville, f + 2*s)
        
        answer += 1

    return answer
