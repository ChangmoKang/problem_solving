# 배상 비용 최소화
import heapq

def solution(N, works):
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(N):
        if works[0] == 0:
            return 0
        else:
            target_value = heapq.heappop(works)
            target_value += 1
            heapq.heappush(works, target_value)

    return sum(work**2 for work in works)


if __name__ == "__main__":
    INPUT1 = [
        4,
        2
    ]
    INPUT2 = [
        [4, 3, 3],
        [3, 3, 3]
    ]
    ANSWER = [
        12,
        17
    ]
    
    for index in range(len(ANSWER)):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)
