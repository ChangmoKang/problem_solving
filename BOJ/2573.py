import sys
from itertools import product
sys.stdin = open('input/2573.txt')
input = sys.stdin.readline


WATER = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
ice = set((r, c) for r, c in product(range(R), range(C)) if board[r][c] != WATER)

time = 0
while ice:
    visited = set()
    r, c = ice.pop()

    ice.add((r, c))
    visited.add((r, c))

    q = [[r, c]]
    while q:
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if (rr, cc) not in visited and board[rr][cc] != WATER:
                    visited.add((rr, cc))
                    q.append([rr, cc])
    
    if ice - visited != set():
        break
    
    time += 1

    side = {}
    for r, c in ice:
        cnt = 0
        for x in range(4):
            rr, cc = r + dr[x], c + dc[x]
            if board[rr][cc] == WATER:
                cnt += 1
        
        if cnt:
            side[r, c] = cnt

    for loc, cnt in side.items():
        r, c = loc
        board[r][c] -= cnt
        if board[r][c] <= 0:
            board[r][c] = WATER
            ice.remove((r, c))

print(time if ice else 0)
