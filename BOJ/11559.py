import sys
from itertools import product
sys.stdin = open('input/11559.txt')


def bfs(loc):
    q = [loc]
    
    while q:
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and board[rr][cc] == board[i][j]:
                    visited[rr][cc] = True
                    q.append([rr, cc])
                    target.append([rr, cc])


EMPTY = '.'
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = 6, 12
board = [list(input()) for _ in range(C)]
board = list(map(list, zip(*board)))

cnt = 0
while True:
    flag = False
    visited = [[False]*C for _ in range(R)]
    for i, j in product(range(R), range(C)):
        if board[i][j] != EMPTY and not visited[i][j]:
            visited[i][j] = True

            target = [[i, j]]
            bfs([i, j])

            if len(target) >= 4:
                for r, c in target:
                    board[r][c] = EMPTY
                flag = True
    
    if not flag:
        break

    for i in range(R):
        tmp = [block for block in board[i] if block != EMPTY]
        board[i] = [EMPTY]*(C - len(tmp)) + tmp
    
    cnt += 1

print(cnt)
