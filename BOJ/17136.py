import sys
sys.stdin = open('input/17136.txt')


def init():
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                check(r, c)
                return False
    return True


def check(r, c):
    global result
    sub_result = 25 - sum(paper)
    if result > sub_result:
        if r == N:
            result = sub_result
        else:
            for size in range(5, 0, -1):
                if paper[size] and search(r, c, size):
                    do(r, c, size, 0)
                    paper[size] -= 1
                    rr, cc = r, c
                    while True:
                        if cc == N - 1:
                            rr += 1
                            cc = 0
                        else:
                            cc += 1

                        if rr == N:
                            check(rr, cc)
                            break
                            
                        if board[rr][cc]:
                            check(rr, cc)
                            break
                    do(r, c, size, 1)
                    paper[size] += 1


def search(r, c, size):
    if not (0 <= r + size - 1 < N and 0 <= c + size - 1 < N):
        return False

    for i in range(r, r + size):
        for j in range(c, c + size):
            if board[i][j] == 0:
                return False
    return True


def do(r, c, size, method):
    for i in range(r, r + size):
        for j in range(c, c + size):
            board[i][j] = method


N = 10
board = [list(map(int, input().split())) for _ in range(N)]

result = 26
paper = [0] + [5]*5
print(0) if init() else print(-1) if result == 26 else print(result)
