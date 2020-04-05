def solution(budgets, M):
    if M >= sum(budgets):
        return max(budgets)
    
    budgets.sort()
    
    l, r = 1, budgets[-1]
    
    while l <= r:
        m = (l + r) // 2
        
        cond = sum(min(m, b) for b in budgets)
        
        if cond <= M:
            l = m + 1
        else:
            r = m - 1
    
    return l - 1
