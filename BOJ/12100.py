import sys
from copy import deepcopy as dc
sys.stdin = open('input/12100.txt')


def go(target, method):
    global result

    if method in 'UD':
        target = list(map(list, zip(*target)))
        target = go(target, op[method])
        target = list(map(list, zip(*target)))
    else:
        for i, t in enumerate(target):
            target[i] = [elem for elem in t if elem != EMPTY]
            temp = []
            if method == 'R':
                target[i] = target[i][::-1]
            wait = EMPTY
            for elem in target[i]:
                if wait == EMPTY:
                    wait = elem
                else:
                    if elem == wait:
                        temp.append(2*elem)
                        wait = EMPTY
                    else:
                        temp.append(wait)
                        wait = elem
            
            if wait != EMPTY:
                temp.append(wait)


            if temp and max(temp) > result:
                result = max(temp)

            temp.extend([0]*(N - len(temp)))
            if method == 'R':
                temp = temp[::-1]
            target[i] = temp

    return target


EMPTY = 0
d = ['U', 'D', 'L', 'R']
op = {'U':'L', 'D':'R'}
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

q = [board]
cnt = 0
while cnt < 5:
    qs, q = q, []
    for b in qs:
        for m in d:
            target = dc(b)
            target = go(target, m)
            q.append(target)
    
    cnt += 1

print(result)
