import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        if works[0] == 0:
            return 0
        
        heapq.heappush(works, heapq.heappop(works) + 1)
        
    return sum(work**2 for work in works)