def solution(N):
    if N == 1:
        return 4
    
    a, b = 1, 1
    for _ in range(2, N):
        a, b = b, a + b
        
    return 2*a + 4*b
