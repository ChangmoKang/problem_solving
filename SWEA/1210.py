import sys
sys.stdin = open('input/1210.txt')


def check(r, c, d):
    if r == 0:
        return c
    else:
        if d == 2:
            for x in range(3):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == 1:
                    return check(rr, cc, x)
        elif d == 0:
            cc = c + dc[d]
            if cc < 0 or board[r][cc] == 0:
                return check(r - 1, c, 2)
            else:
                return check(r, cc, 0)
        else:
            cc = c + dc[d]
            if cc >= N or board[r][cc] == 0:
                return check(r - 1, c, 2)
            else:
                return check(r, cc, 1)


dr = [0, 0, -1]
dc = [-1, 1, 0]
N = 100
for _ in range(10):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    for j in range(N):
        if board[N - 1][j] == 2:
            c = j
            break

    print(f"#{tc} {check(99, c, 2)}")
