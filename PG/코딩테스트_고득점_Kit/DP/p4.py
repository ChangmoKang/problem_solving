from itertools import product

DIVISOR = 1_000_000_007
def solution(m, n, puddles):
    p = {(r - 1, c - 1) for c, r in puddles}
    board = [[0]*m for _ in range(n)]

    board[0][0] = 1
    for r, c in product(range(n), range(m)):
        if (r == 0 and c == 0) or (r, c) in p:
            continue
            
        board[r][c] = (board[r - 1][c] + board[r][c - 1]) % DIVISOR

    return board[-1][-1]
