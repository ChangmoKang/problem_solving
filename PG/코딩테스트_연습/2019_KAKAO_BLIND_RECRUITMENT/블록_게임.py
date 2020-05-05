from itertools import product


EMPTY, BLACK = 0, 201


def solution(board):
    
    def visitable(i, j):
        return True if (0 <= i < N and 0 <= j < N) else False
    
    
    def stack_black_block():
        for c in range(N):
            for r in range(N):
                if board[r][c] != EMPTY:
                    for w in range(1, 3):
                        if visitable(r - w, c):
                            board[r - w][c] = BLACK
                        else:
                            break
                    break
                    
    
    def check_destroyable_block(r_range, c_range):
        nonlocal flag, answer
        temp = {}
        for dr, dc in product(range(r_range), range(c_range)):
            if visitable(r + dr, c + dc) and board[r + dr][c + dc] != EMPTY:
                if board[r + dr][c + dc] not in temp:
                    temp[board[r + dr][c + dc]] = 1
                else:
                    temp[board[r + dr][c + dc]] += 1
            else:
                break
        else:
            if len(temp) == 2 and BLACK in temp and temp[BLACK] == 2:
                answer += 1
                flag = True
                for dr, dc in product(range(r_range), range(c_range)):
                    board[r + dr][c + dc] = EMPTY
                    
                    
    def remove_black_block():
        for r, c in product(range(N), range(N)):
            if board[r][c] == BLACK:
                board[r][c] = EMPTY
                
                
    N = len(board)
    
    answer = 0
    while True:
        flag = False
        
        stack_black_block()

        for r, c in product(range(N), range(N)):
            if board[r][c] != EMPTY:
                check_destroyable_block(2, 3)
                check_destroyable_block(3, 2)

        if not flag:
            break
        
        remove_black_block()
                
    return answer
