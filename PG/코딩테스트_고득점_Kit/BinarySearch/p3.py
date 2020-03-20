def solution(distance, rocks, n):
    target_interval_count = len(rocks) + 1 - n
    rocks = [0] + sorted(rocks) + [distance]
    
    l, r = 1, distance
    
    while l <= r:
        m = (l + r) // 2
        
        interval_distance = 0
        interval_count = 0
        for i in range(len(rocks) - 1):
            interval_distance += rocks[i + 1] - rocks[i]
            if interval_distance >= m:
                interval_count += 1
                interval_distance = 0
        
        if interval_distance:
            interval_count -= 1
        
        if interval_count < target_interval_count:
            r = m - 1
        else:
            l = m + 1
    
    return l - 1
