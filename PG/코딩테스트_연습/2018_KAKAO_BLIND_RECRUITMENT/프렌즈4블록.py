from itertools import product

EMPTY = ''
def solution(m, n, board):
    R, C = n, m
    board = list(map(list, zip(*board)))

    answer = 0
    while True:
        destroy = set()
        
        for i, j in product(range(R - 1), range(C - 1)):
            if board[i][j] != EMPTY:
                for r, c in product(range(i, i+2), range(j, j+2)):
                    if board[i][j] != board[r][c]:
                        break
                else:
                    for r, c in product(range(i, i+2), range(j, j+2)):
                        destroy.add((r, c))
        
        if not destroy:
            break
            
        answer += len(destroy)
        
        for rr, cc in destroy:
            board[rr][cc] = EMPTY
            
        for r in range(R):
            board[r] = [b for b in board[r] if b != EMPTY]
            board[r] = [EMPTY]*(C - len(board[r])) + board[r]
            
    return answer
