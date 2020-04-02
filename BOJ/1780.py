import sys
sys.stdin = open('input/1780.txt')


KIND = [-1, 0, 1]
dr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dc = [0, 1, 2, 0, 1, 2, 0, 1, 2]
def check(r, c, l):
    if l == N:
        for k in KIND:
            if inspect(r, c, l, k):
                paper[k] += 1
                return

    third = l // 3
    for x in range(9):
        rr, cc = r + dr[x] * third, c + dc[x] * third
        for k in KIND:
            if inspect(rr, cc, third, k):
                paper[k] += 1
                break
        else:
            check(rr, cc, third)



def inspect(r, c, l, k):
    for i in range(r, r + l):
        for j in range(c, c + l):
            if board[i][j] != k:
                return False
    return True


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
paper = [0]*3
check(0, 0, N)

for i in range(-1, 2):
    print(paper[i])
