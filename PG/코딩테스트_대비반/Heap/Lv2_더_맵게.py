import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville, f + 2*s)

        answer += 1

    return answer
