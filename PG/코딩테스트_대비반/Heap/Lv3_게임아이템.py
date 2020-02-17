import heapq

def solution(healths, items):
    healths.sort()
    healths_visited = [0]*len(healths)
    
    items = [[-item[0], item[1], item_index + 1] for item_index, item in enumerate(items)]
    heapq.heapify(items)
    
    answer = []
    while items:
        _, damage, index = heapq.heappop(items)

        for health_index, health in enumerate(healths):
            if not healths_visited[health_index]:
                if health - damage >= 100:
                    healths_visited[health_index] = 1
                    answer.append(index)
                    break
        
    answer.sort()
    return answer
