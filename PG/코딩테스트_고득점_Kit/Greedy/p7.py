def solution(weight):
    weight.sort()
    
    max_range = 0
    for w in weight:
        if w > max_range + 1:
            return max_range + 1
        else:
            max_range += w

    return max_range + 1
