from string import ascii_uppercase as A_TO_Z

UP = {alphabet: i for i, alphabet in enumerate(A_TO_Z)}
DOWN = {alphabet: len(A_TO_Z) - i for i, alphabet in enumerate(A_TO_Z)}

def solution(name):
    v = [min(UP[alphabet], DOWN[alphabet]) for alphabet in name]
    answer = sum(v)
    
    index = 0
    if not v[0]:
        l = r = index
        cnt = 0
        while True:
            l = len(v) - 1 if l == 0 else l - 1
            r = 0 if r == len(v) - 1 else r + 1
                
            cnt += 1
            if cnt == len(v):
                return 0
            
            if v[l]:
                index = l
                break
                
            if v[r]:
                index = r
                break

    while True:
        v[index] = 0
        
        l = r = index
        cnt = 0
        while True:
            l = len(v) - 1 if l == 0 else l - 1
            r = 0 if r == len(v) - 1 else r + 1
                
            cnt += 1
            if cnt == len(v):
                return answer
            
            if v[l]:
                index = l
                break
                
            if v[r]:
                index = r
                break

        answer += cnt
