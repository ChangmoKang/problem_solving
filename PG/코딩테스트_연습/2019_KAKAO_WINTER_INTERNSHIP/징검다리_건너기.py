def solution(stones, k):
    l, r = 1, max(stones)
    
    while l <= r:
        m = (l + r) // 2
        
        temp_stones = [max(stone - m, 0) for stone in stones]
        
        t = -1
        for i, s in enumerate(temp_stones):
            if not s:
                continue
                
            if i - t > k:
                r = m - 1
                break
        
            t = i
        else:
            if i + 1 - t > k:
                r = m - 1
            else:
                l = m + 1
    
    return r + 1