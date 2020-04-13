from itertools import chain
from collections import Counter


MIN, MAX = 0, 10_0000_0000
def solution(land, P, Q):
    def calc(mid):
        return sum([(h - mid)*cnt*Q if h - mid >= 0 else (mid - h)*cnt*P for h, cnt in land.items()])

    
    land = Counter(chain(*land))
    l, r = 0, max(land)
    save = {}
    while l <= r:
        m = (l + r) // 2
        
        cond1 = calc(m)
        save[m] = cond1

        cond2 = calc(m + 1)
        save[m + 1] = cond2
        
        if cond1 == cond2:
            break

        if cond2 > cond1:
            r = m - 1
        else:
            l = m + 1

    answer = float('inf')
    for i in range(m - 1, m + 2):
        if not (MIN <= i <= MAX):
            continue

        if i in save:
            temp = save[i]
        else:
            temp = calc(i)

        if answer > temp:
            answer = temp

    return answer
