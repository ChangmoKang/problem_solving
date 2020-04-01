import sys
sys.stdin = open('input/2630.txt')


def check(r, rr, c, cc):
    for k in range(2):
        if inspect(r, rr, c, cc, k):
            return

    check(r, (r + rr)//2, c, (c + cc)//2)
    check(r, (r + rr)//2, (c + cc)//2, cc)
    check((r + rr)//2, rr, c, (c + cc)//2)
    check((r + rr)//2, rr, (c + cc)//2, cc)


def inspect(r, rr, c, cc, k):
    for i in range(r, rr):
        for j in range(c, cc):
            if board[i][j] != k:
                return False

    paper[k] += 1
    return True


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

paper = [0]*2
check(0, N, 0, N)

for p in paper:
    print(p)
