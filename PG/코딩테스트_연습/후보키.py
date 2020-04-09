from itertools import combinations

def solution(relation):
    def possible_key():
        for key in keys:
            count = 0
            for k in key:
                if k in cand:
                    count +=1
            if count == len(key):
                return False
    
        return True
    
    
    R, C = len(relation), len(relation[0])
    
    result = 0
    
    keys = set()
    for c in range(C):
        target = [rel[c] for rel in relation]
        if len(set(target)) == R:
            keys.add(c)
    result += len(keys)
    
    cands = list(set(range(C)) - keys)
    
    keys = []
    for cnt in range(2, C + 1):
        for cand in combinations(cands, cnt):
            if not possible_key():
                continue
                
            target = set()
            for r in range(R):
                tmp = []
                for c in cand:
                    tmp.append(relation[r][c])
                target.add(tuple(tmp))
            
            if len(target) == R:
                keys.append(cand)
    
    result += len(keys)
    
    return result
