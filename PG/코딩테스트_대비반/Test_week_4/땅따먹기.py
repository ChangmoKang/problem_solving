def solution(land):
    R, C = len(land), 4
       
    for r in range(1, R):
        for c in range(C):
            land[r][c] = land[r][c] + max(land[r - 1][:c] + land[r - 1][c + 1:])
    
    return max(land[-1])
