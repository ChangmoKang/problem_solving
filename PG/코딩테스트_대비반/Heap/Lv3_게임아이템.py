import heapq
from collections import deque

def solution(healths, items):
    ATTACK, DAMAGE, IDX = 0, 1, 2
    
    healths.sort()
    items = deque(sorted([(*item, idx) for idx, item in enumerate(items, 1)], key=lambda x: x[DAMAGE]))

    answer = []
    available_items = []
    for health in healths:
        while items and health - items[0][DAMAGE] >= 100:
            target_item = items.popleft()
            heapq.heappush(available_items, (-target_item[ATTACK], target_item[IDX]))
        if available_items:
            answer.append(heapq.heappop(available_items)[1])

    answer.sort()
    return answer
