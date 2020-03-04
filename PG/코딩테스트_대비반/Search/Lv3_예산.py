def solution(budgets, M):
    if M >= sum(budgets):
        return max(budgets)

    l, r = 1, max(budgets)
    
    while l <= r:
        m = (l + r) // 2
        
        temp_budgets = sum(m if budget > m else budget for budget in budgets)
        
        if temp_budgets > M:
            r = m - 1
        else:
            l = m + 1

    return l - 1
