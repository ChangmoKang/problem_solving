import re

bonus = {'S' : 1, 'D' : 2, 'T' : 3}
option = {'' : 1, '*' : 2, '#' : -1}
SCORE, BONUS, OPTION = 0, 1, 2
def solution(dartResult):
    p = re.compile('(\d+)([SDT])([*#]?)')
    darts = p.findall(dartResult)
    
    for i, dart in enumerate(darts):
        if i > 0 and dart[OPTION] == '*':
            darts[i - 1] *= 2
        darts[i] = int(dart[SCORE]) ** bonus[dart[BONUS]] * option[dart[OPTION]]
        
    return sum(darts)
