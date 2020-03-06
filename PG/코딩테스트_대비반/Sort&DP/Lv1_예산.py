def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    
    d.sort()
    
    v = 0
    for count, elem in enumerate(d):
        v += elem
        if v > budget:
            break
            
    return count
