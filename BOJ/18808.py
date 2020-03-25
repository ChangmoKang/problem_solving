import sys
sys.stdin = open('input/18808.txt')


def search():
    for i in range(N):
        for j in range(M):
            if check(i, j, sticker):
                install(i, j, sticker)
                return True
    return False


def check(i, j, s):
    R, C = len(s), len(s[0])

    for r in range(R):
        for c in range(C):
            if s[r][c]:
                if not (0 <= i + r < N and 0 <= j + c < M):
                    return False

                if board[i + r][j + c]:
                    return False
    return True


def install(i, j, s):
    R, C = len(s), len(s[0])

    for r in range(R):
        for c in range(C):
            if s[r][c]:
                board[i + r][j + c] = 1


N, M, K = map(int, input().split())

board = [[0]*M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())

    sticker = [list(map(int, input().split())) for _ in range(R)]

    for _ in range(4):
        if search():
            break

        R, C = len(sticker), len(sticker[0])
        rotate_90 = [[0]*R for _ in range(C)]
        for r in range(R):
            for c in range(C):
                if sticker[r][c]:
                    rotate_90[c][(R - 1) - r] = 1

        sticker = rotate_90

print(sum(sum(b) for b in board))
