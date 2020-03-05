def solution(l, v):
    v.sort()
    min_d = max(l - v[-1], v[0])
    
    for i in range(len(v) - 1):
        overlap_d = (v[i + 1] - v[i] + 1) // 2
        min_d = max(overlap_d, min_d)

    return min_d
