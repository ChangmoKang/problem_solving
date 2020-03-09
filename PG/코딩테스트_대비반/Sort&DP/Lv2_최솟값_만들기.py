def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    return sum(a*b for a, b in zip(A, B))
