def solution(food_times, k):
    l, r = 0, max(food_times)
    total_food_time = sum(food_times)
    while l <= r:
        m = (l + r) // 2
        
        cond = sum(m if food >= m else food for food in food_times)
        
        if cond > k:
            r = m - 1
        else:
            l = m + 1    

    food_times = [food - (l - 1) if food >= l - 1 else 0 for food in food_times]
    k -= total_food_time - sum(food_times)
    
    idx = 0
    for i, food in enumerate(food_times):
        if food > 0:
            if idx == k:
                return i + 1
            else:
                idx += 1
    return -1
