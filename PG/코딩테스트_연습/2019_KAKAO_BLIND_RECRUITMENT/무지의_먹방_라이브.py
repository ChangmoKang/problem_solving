def solution(food_times, k):
    l, r = 0, sum(food_times)
    
    while l <= r:
        m = (l + r) // 2
        
        cond = sum(m if food - m >= 0 else food for food in food_times)
        
        if cond <= k:
            l = m + 1
        else:
            r = m - 1
            
    round_ = l - 1
    ate = [round_ if food - round_ >= 0 else food for food in food_times]
    
    k -= sum(ate)
    
    for i, food in enumerate(food_times):
        if food - ate[i]:
            if not k:
                return i + 1
            k -= 1
    
    return -1
