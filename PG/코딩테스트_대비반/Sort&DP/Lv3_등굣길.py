def solution(R, C, puddles):
    DIVISOR = 1000000007

    board = [[0]*C for _ in range(R)]
    puddles = set([(r - 1, c - 1) for r, c in puddles])
    board[0][0] = 1

    for r in range(R):
        for c in range(C):
            if (r == 0 and c == 0) or (r, c) in puddles:
                continue
            board[r][c] = (board[r - 1][c] + board[r][c - 1]) % DIVISOR

    return board[R - 1][C - 1]
