import sys
sys.stdin = open('input/1992.txt')


KIND = ['0', '1']
dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]
def check(r, c, l):
    global result

    for k in KIND:
        if inspect(r, c, l, k):
            result += k
            return

    result += '('
    half = l // 2
    for x in range(4):
        rr, cc = r + dr[x] * half, c + dc[x] * half
        for k in KIND:
            if inspect(rr, cc, half, k):
                result += k
                break
        else:
            check(rr, cc, half)

    result += ')'


def inspect(r, c, l, k):
    for i in range(r, r + l):
        for j in range(c, c + l):
            if board[i][j] != k:
                return False
    return True


N = int(input())
board = [list(input()) for _ in range(N)]
result = ''
check(0, 0, N)

print(result)
