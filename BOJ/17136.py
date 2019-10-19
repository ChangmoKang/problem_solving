import sys
sys.stdin = open('input/17136.txt')


def get_or_out_area(r, c, k, method):
    if method:
        for i in range(r, r + k):
            for j in range(c, c + k):
                board[i][j] = 0
    else:
        for i in range(r, r + k):
            for j in range(c, c + k):
                board[i][j] = 1


def check_area(r, c):
    for k in range(5, 1, -1):
        if r + k > N or c + k > N:
            continue
        flag = 0
        for i in range(r, r + k):
            for j in range(c, c + k):
                if board[i][j] == 0:
                    flag = 1
                    break
            if flag:
                break
        if not flag:
            return k
    return 1


def move(r, c):
    if c == N - 1:
        r += 1
        c = 0
    else:
        c += 1
    return r, c


def check(r, c, cnt):
    global result
    if cnt == room:
        if result > 25 - sum(paper):
            result = 25 - sum(paper)
    else:
        if result > 25 - sum(paper):
            while True:
                if board[r][c]:
                    break
                r, c = move(r, c)
                if r == N:
                    return

            RANGE = check_area(r, c)
            for k in range(RANGE, 0, -1):
                if paper[k]:
                    get_or_out_area(r, c, k, 1)
                    paper[k] -= 1

                    check(r, c, cnt + (k*k))
                    paper[k] += 1
                    get_or_out_area(r, c, k, 0)


N = 10
board = [list(map(int, input().split())) for _ in range(N)]

room = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            room += 1

if room:
    result = 26
    paper = [0] + [5]*5
    check(0, 0, 0)
    print(result) if result != 26 else print(-1)
else:
    print(0)

