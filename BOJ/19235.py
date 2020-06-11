import sys
sys.stdin = open('input/19235.txt')


def stack(c, index, method):
    if method == 1:
        for rr in range(R):
            if board[index][rr][c] == FULL:
                board[index][rr - 1][c] = FULL
                break
        else:
            board[index][rr][c] = FULL

    elif method == 2:
        for rr in range(R):
            if board[index][rr][c] == FULL or board[index][rr][c + 1] == FULL:
                board[index][rr - 1][c] = FULL
                board[index][rr - 1][c + 1] = FULL
                break
        else:
            board[index][rr][c] = FULL
            board[index][rr][c + 1] = FULL

    elif method == 3:
        for rr in range(R):
            if board[index][rr][c] == FULL:
                board[index][rr - 2][c] = FULL
                board[index][rr - 1][c] = FULL
                break
        else:
            board[index][rr - 1][c] = FULL
            board[index][rr][c] = FULL

    
def score():
    global answer

    for index in range(2):
        for r in range(R - 1, -1, -1):
            if sum(board[index][r]) == C:
                answer += 1
                board[index][r] = [EMPTY]*C
                for c in range(C):
                    for rr in range(r - 1, -1, -1):
                        if board[index][rr][c] == FULL:
                            for rrr in range(rr + 1, R):
                                if board[index][rrr][c] == FULL:
                                    board[index][rr][c] = EMPTY
                                    board[index][rrr - 1][c] = FULL
                                    break
                            else:
                                board[index][rr][c] = EMPTY
                                board[index][rrr][c] = FULL
                return True
    return False


def pop():
    for index in range(2):
        for _ in range(2):
            if sum(board[index][1]):
                board[index].pop()
                board[index].insert(0, [EMPTY]*C)


R, C = 6, 4
EMPTY, FULL = range(2)
CHANGE = {1: 1, 2: 3, 3: 2}

board = [
    [[EMPTY]*C for _ in range(R)],
    [[EMPTY]*C for _ in range(R)]
]

answer = 0
for _ in range(int(input())):
    t, i, j= map(int, input().split())

    stack(j, 0, t)
    stack(i, 1, CHANGE[t])

    while True:
        if not score():
            break

    pop()

cnt = 0
for index in range(2):
    for r in range(2, R):
        for c in range(C):
            if board[index][r][c]:
                cnt += 1

print(answer)
print(cnt)