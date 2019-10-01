import sys
sys.stdin = open('input/5656.txt')


def destroy_brick(info, board, bricks):
    q = [info]
    board[info[0]][info[1]] = 0
    bricks -= 1

    while q and bricks:
        content = q.pop()
        for i in range(4):
            for weight in range(1, content[2]):
                r = content[0] + weight * dr[i]
                c = content[1] + weight * dc[i]
                if 0 <= r < R and 0 <= c < C:
                    if board[r][c]:
                        q.append([r, c, board[r][c]])
                        board[r][c] = 0
                        bricks -= 1
                else:
                    break

    return board, bricks


def move_brick(board):
    for i in range(R - 2, -1, -1):
        for j in range(C):
            if board[i][j]:
                for idx in range(R - 1, i, - 1):
                    if board[idx][j] == 0:
                        board[i][j], board[idx][j] = board[idx][j], board[i][j]
                        break
    return board


def check(shots, bricks, board):
    global result

    if not shots or not bricks:
        if result > bricks:
            result = bricks
    else:
        for j in range(C):
            for i in range(R):
                if result and board[i][j]:
                    copied_board = [board[w][:] for w in range(R)]                    
                    copied_board, copied_bricks = destroy_brick([i, j, copied_board[i][j]], copied_board, bricks)

                    if copied_bricks:
                        copied_board = move_brick(copied_board)
                        check(shots - 1, copied_bricks, copied_board)
                    else:
                        result = 0
                        return
                    break


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, C, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    
    init_bricks = 0
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                init_bricks += 1

    result = init_bricks
    check(N, init_bricks, board)
    print(f"#{tc} {result}")
