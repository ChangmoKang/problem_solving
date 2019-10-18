import sys
sys.stdin = open('input/17144.txt')


def find_robot():
    for i in range(R):
        if board[i][0] == -1:
            return [[i, 0], [i + 1, 0]]


def spread():
    add_board = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] >= 5:
                cnt = 0
                el = int(board[r][c]/5)
                for x in range(4):
                    rr = r + dr[x]
                    cc = c + dc[x]
                    if 0 <= rr < R and 0 <= cc < C and [rr, cc] not in robot:
                        add_board[rr][cc] += el
                        cnt += 1
                if cnt:
                    board[r][c] -= cnt * el

    for i in range(R):
        for j in range(C):
            if add_board[i][j]:
                board[i][j] += add_board[i][j]


def rotate():
    r1 = robot[0][0]
    r2 = robot[1][0]

    tmp1 = 0
    tmp2 = None
    for c in range(1, C):
        if tmp1 == None:
            tmp1 = board[r1][c]
            board[r1][c] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[r1][c]
            board[r1][c] = tmp1
            tmp1 = None

    for r in range(r1 - 1, -1, -1):
        if tmp1 == None:
            tmp1 = board[r][C - 1]
            board[r][C - 1] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[r][C - 1]
            board[r][C - 1] = tmp1
            tmp1 = None

    for c in range(C - 2, -1, -1):
        if tmp1 == None:
            tmp1 = board[0][c]
            board[0][c] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[0][c]
            board[0][c] = tmp1
            tmp1 = None

    for r in range(1, r1):
        if tmp1 == None:
            tmp1 = board[r][0]
            board[r][0] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[r][0]
            board[r][0] = tmp1
            tmp1 = None

    tmp1 = 0
    tmp2 = None
    for c in range(1, C):
        if tmp1 == None:
            tmp1 = board[r2][c]
            board[r2][c] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[r2][c]
            board[r2][c] = tmp1
            tmp1 = None

    for r in range(r2 + 1, R):
        if tmp1 == None:
            tmp1 = board[r][C - 1]
            board[r][C - 1] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[r][C - 1]
            board[r][C - 1] = tmp1
            tmp1 = None

    for c in range(C - 2, -1, -1):
        if tmp1 == None:
            tmp1 = board[R - 1][c]
            board[R - 1][c] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[R - 1][c]
            board[R - 1][c] = tmp1
            tmp1 = None

    for r in range(R - 2, r2, -1):
        if tmp1 == None:
            tmp1 = board[r][0]
            board[r][0] = tmp2
            tmp2 = None
        elif tmp2 == None:
            tmp2 = board[r][0]
            board[r][0] = tmp1
            tmp1 = None


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

robot = find_robot()

for _ in range(T):
    spread()
    rotate()

print(sum([board[i][j] for i in range(R) for j in range(C) if board[i][j] > 0]))
