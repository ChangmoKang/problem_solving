import sys
from itertools import product
sys.stdin = open('input/13460.txt')


def move(method, red, blue):
    if method == 0:
        if red[C] == blue[C]:
            if red[R] < blue[R]:
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        red = (r, c)
                        break
                
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        blue = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == red:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

            else:
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        blue = (r, c)
                        break
                
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        red = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == blue:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

        else:
            r, c = red
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    red = (r, c)
                    break

                elif board[r][c] == EXIT:
                    red = (r, c)
                    break

            r, c = blue
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == EXIT:
                    blue = (r, c)
                    break

                elif board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    blue = (r, c)
                    break



    elif method == 1:
        if red[C] == blue[C]:
            if red[R] > blue[R]:
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        red = (r, c)
                        break
                
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        blue = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == red:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

            else:
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        blue = (r, c)
                        break
                
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        red = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == blue:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

        else:
            r, c = red
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    red = (r, c)
                    break

                elif board[r][c] == EXIT:
                    red = (r, c)
                    break

            r, c = blue
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    blue = (r, c)
                    break

                elif board[r][c] == EXIT:
                    blue = (r, c)
                    break


    elif method == 2:
        if red[R] == blue[R]:
            if red[C] < blue[C]:
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        red = (r, c)
                        break
                
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        blue = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == red:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

            else:
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        blue = (r, c)
                        break
                
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        red = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == blue:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

        else:
            r, c = red
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    red = (r, c)
                    break

                elif board[r][c] == EXIT:
                    red = (r, c)
                    break

            r, c = blue
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    blue = (r, c)
                    break

                elif board[r][c] == EXIT:
                    blue = (r, c)
                    break


    else:
        if red[R] == blue[R]:
            if red[C] > blue[C]:
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        red = (r, c)
                        break
                
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        blue = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == red:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

            else:
                r, c = blue
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == WALL:
                        r -= dr[method]
                        c -= dc[method]
                        blue = (r, c)
                        break

                    elif board[r][c] == EXIT:
                        blue = (r, c)
                        break
                
                r, c = red
                while True:
                    r += dr[method]
                    c += dc[method]

                    if board[r][c] == EXIT:
                        red = (r, c)
                        break

                    elif board[r][c] == WALL or (r, c) == blue:
                        r -= dr[method]
                        c -= dc[method]
                        red = (r, c)
                        break

        else:
            r, c = red
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    red = (r, c)
                    break

                elif board[r][c] == EXIT:
                    red = (r, c)
                    break

            r, c = blue
            while True:
                r += dr[method]
                c += dc[method]

                if board[r][c] == WALL:
                    r -= dr[method]
                    c -= dc[method]
                    blue = (r, c)
                    break

                elif board[r][c] == EXIT:
                    blue = (r, c)
                    break

    return [red, blue]


def bfs():
    q = [[ori_red, ori_blue]]
    save = set()
    save.add((ori_red, ori_blue))
    cnt = 1
    while q:
        qs, q = q, []
        for target_red, target_blue in qs:

            for x in range(4):
                new_r, new_b = move(x, target_red, target_blue)
                if (new_r, new_b) not in save:
                    if board[new_b[R]][new_b[C]] == EXIT:
                        continue

                    if board[new_r[R]][new_r[C]] == EXIT:
                        return cnt
                    q.append([new_r, new_b])
                    save.add((new_r, new_b))

        cnt += 1
        if cnt == 11:
            break

    return -1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C, EMPTY, WALL, EXIT = 0, 1, '.', '#', 'O'

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for r, c, in product(range(N), range(M)):
    if board[r][c] == 'R':
        ori_red = (r, c)
        board[r][c] = EMPTY
    elif board[r][c] == 'B':
        ori_blue = (r, c)
        board[r][c] = EMPTY

print(bfs())
