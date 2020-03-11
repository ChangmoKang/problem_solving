import heapq
from collections import deque

def solution(stock, dates, supplies, k):
    answer = 0
    dates = deque(dates)
    supplies = deque(supplies)
    
    candidate = []
    while stock < k:
        while dates and dates[0] <= stock:
            dates.popleft()
            heapq.heappush(candidate, -supplies.popleft())
            
        answer += 1
        stock += -heapq.heappop(candidate)
            
    return answer
