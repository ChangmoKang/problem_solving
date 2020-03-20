def solution(n, times):
    l, r = 1, max(times) * n
    
    while l <= r:
        m = (l + r) // 2
        
        target = sum(m // time for time in times)
        
        if target >= n:
            r = m - 1
        else:
            l = m + 1
            
    return r + 1
