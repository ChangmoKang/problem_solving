from itertools import combinations


def solution(relation):
    
    def check_minimality(target_key):
        for j in range(1, len(target_key) + 1):
            for comb in combinations(target_key, j):
                if comb in result:
                    return False
        return True
    
    
    def check_uniqueness(target_key):
        x = [tuple(relation[r][c] for c in target_key) for r in range(R)]
        return True if len(x) == len(set(x)) else False
    
    
    R, C = len(relation), len(relation[0])
    
    result = set()
    for i in range(1, C + 1):
        for key in combinations(range(C), i):
            if check_minimality(key) and check_uniqueness(key):
                result.add(key)
    
    return len(result)
