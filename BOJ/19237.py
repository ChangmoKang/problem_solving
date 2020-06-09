import sys
from itertools import product
sys.stdin = open('input/c.txt')


def is_empty(r, c):
    for x in range(1, 5):
        rr, cc = r + D[x][R], c + D[x][C]
        if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == EMPTY:
            return True
    return False


D = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1),
}

EMPTY = 0
R, C = 0, 1
ANT, POWER, DIRECTION = 0, 1, 2
N, M, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ant = {}
ant_dir = list(map(int, input().split()))
for i, j in product(range(N), range(N)):
    if board[i][j] != EMPTY:
        ant[i, j] = [board[i][j], ant_dir[board[i][j] - 1]]
        board[i][j] = [board[i][j], W]

pri = {}
for index in range(1, M + 1):
    pri[index] = [0] + [list(map(int, input().split())) for _ in range(4)]

for t in range(1, 1001):
    new_ant = {}
    new_board = [b[:] for b in board]
    for r, c in ant:
        index, d = ant[r, c]

        if is_empty(r, c):
            for x in pri[index][d]:
                rr, cc = r + D[x][R], c + D[x][C]
                if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == EMPTY:
                    if (rr, cc) not in new_ant:
                        new_ant[rr, cc] = [index, x]
                        new_board[rr][cc] = [index, W]
                    else:
                        if new_ant[rr, cc][ANT] > index:
                            new_ant[rr, cc] = [index, x]
                            new_board[rr][cc] = [index, W]
                    break
        else:
            for x in pri[index][d]:
                rr, cc = r + D[x][R], c + D[x][C]
                if 0 <= rr < N and 0 <= cc < N and board[rr][cc][ANT] == index:
                    new_ant[rr, cc] = [index, x]
                    new_board[rr][cc][POWER] = W
                    break

    if len(new_ant) == 1:
        print(t)
        break

    ant = {key: value[:] for key, value in new_ant.items()}
    board = [n_b[:] for n_b in new_board]

    for i, j in product(range(N), range(N)):
        if board[i][j] != EMPTY and (i, j) not in ant:
            board[i][j][POWER] -= 1
            if board[i][j][POWER] == 0:
                board[i][j] = EMPTY
else:
    print(-1)