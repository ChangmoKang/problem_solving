import sys
sys.stdin = open('input/19235.txt')


def stack(c, index, method):
    if method == 1:
        for rr in range(R):
            if board[index][rr][c] != EMPTY:
                board[index][rr - 1][c] = tile
                break
        else:
            board[index][rr][c] = tile

    elif method == 2:
        for rr in range(R):
            if board[index][rr][c] != EMPTY or board[index][rr][c + 1] != EMPTY:
                board[index][rr - 1][c] = tile
                board[index][rr - 1][c + 1] = tile
                break
        else:
            board[index][rr][c] = tile
            board[index][rr][c + 1] = tile

    elif method == 3:
        for rr in range(R):
            if board[index][rr][c] != EMPTY:
                board[index][rr - 2][c] = tile
                board[index][rr - 1][c] = tile
                break
        else:
            board[index][rr - 1][c] = tile
            board[index][rr][c] = tile

    
def score():
    global answer

    big_flag = False
    for index in range(2):
        flag = None
        for r in range(R):
            if EMPTY not in board[index][r]:
                answer += 1
                board[index][r] = [EMPTY]*C
                flag = r
        if flag is not None:
            big_flag = True
            for rr in range(flag - 1, -1, -1):
                for c in range(C):
                    if board[index][rr][c] != EMPTY:
                        temp = board[index][rr][c]
                        shape = connect(rr, c, index, temp)

                        if shape is None:
                            continue

                        if shape == 1:
                            for rrr in range(rr + 1, R):
                                if board[index][rrr][c] != EMPTY:
                                    board[index][rr][c] = EMPTY
                                    board[index][rrr - 1][c] = temp
                                    break
                            else:
                                board[index][rr][c] = EMPTY
                                board[index][rrr][c] = temp
                        elif shape == 2:
                            for rrr in range(rr + 1, R):
                                if board[index][rrr][c] != EMPTY or board[index][rrr][c + 1] != EMPTY:
                                    board[index][rr][c] = EMPTY
                                    board[index][rr][c + 1] = EMPTY
                                    board[index][rrr - 1][c] = temp
                                    board[index][rrr - 1][c + 1] = temp
                                    break
                            else:
                                board[index][rr][c] = EMPTY
                                board[index][rr][c + 1] = EMPTY
                                board[index][rrr][c] = temp
                                board[index][rrr][c + 1] = temp
                        else:
                            for rrr in range(rr + 1, R):
                                if board[index][rrr][c] != EMPTY:
                                    board[index][rr - 1][c] = EMPTY
                                    board[index][rr][c] = EMPTY
                                    board[index][rrr - 2][c] = temp
                                    board[index][rrr - 1][c] = temp
                                    break
                            else:
                                board[index][rr - 1][c] = EMPTY
                                board[index][rr][c] = EMPTY
                                board[index][rrr - 1][c] = temp
                                board[index][rrr][c] = temp
    return big_flag


def pop():
    for index in range(2):
        for _ in range(2):
            if sum(board[index][1]):
                board[index].pop()
                board[index].insert(0, [EMPTY]*C)


def connect(r, c, index, target):
    for x in range(4):
        rr, cc = r + dr[x], c + dc[x]
        if 0 <= rr < R and 0 <= cc < C and board[index][rr][cc] == target:
            if x == 0:
                return 3
            elif x == 3:
                return 2
            else:
                return None
    return 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
EMPTY = 0
R, C = 6, 4
CHANGE = {1: 1, 2: 3, 3: 2}

board = [
    [[EMPTY]*C for _ in range(R)],
    [[EMPTY]*C for _ in range(R)]
]

answer = 0
for tile in range(1, int(input()) + 1):
    t, i, j= map(int, input().split())

    stack(j, 0, t)
    stack(i, 1, CHANGE[t])

    while True:
        if not score():
            break

    pop()

    # print('--------------------------------------')
    # print(t, i, j)
    # print(*board[0], sep="\n")
    # print()
    # print(*list(map(list, zip(*board[1]))), sep="\n")
    # print('--------------------------------------')


cnt = 0
for index in range(2):
    for r in range(2, R):
        for c in range(C):
            if board[index][r][c]:
                cnt += 1

print(answer)
print(cnt)