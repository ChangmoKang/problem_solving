def solution(n):
    DIVISOR = 1000000007

    if n == 1 or n == 2:
        return n
    
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, (a + b) % DIVISOR
    
    return b
