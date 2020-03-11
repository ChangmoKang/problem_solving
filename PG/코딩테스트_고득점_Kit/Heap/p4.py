import heapq

INSERT = 'I'
def solution(operations):
    max_save = []
    min_save = []
    i_count = d_count = 0
    
    for operation in operations:
        method, number = operation.strip().split()
        if method == INSERT:
            i_count += 1
            heapq.heappush(max_save, -int(number))
            heapq.heappush(min_save, int(number))
        else:
            if i_count > d_count:
                d_count += 1
                if i_count == d_count:
                    max_save.clear()
                    min_save.clear()
                else:
                    if int(number) == 1:
                        heapq.heappop(max_save)
                    else:
                        heapq.heappop(min_save)
                
    return [-heapq.heappop(max_save), heapq.heappop(min_save)] if i_count != d_count else [0, 0]
