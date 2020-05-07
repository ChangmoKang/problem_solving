EMPTY = 0


def solution(board, moves):
    N = len(board)
    
    answer = 0
    stack = []
    for move in moves:
        for r in range(N):
            if board[r][move - 1] != EMPTY:
                if stack and stack[-1] == board[r][move - 1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[r][move - 1])
                    
                board[r][move - 1] = EMPTY
                break
                
    return answer
                