from itertools import product

def solution(m, weights):
    weights = [(0, weight) for weight in weights]
    
    answer = 0
    for case in product(*weights):
        if sum(case) == m:
            answer += 1
    
    return answer