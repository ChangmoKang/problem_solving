from collections import Counter

MUL = 65536
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    
    if not str1 and not str2:
        return MUL
    
    c1 = Counter(str1)
    c2 = Counter(str2)
    
    union = sum((c1|c2).values())
    inter = sum((c1&c2).values())
    
    return int(inter/union*MUL)
