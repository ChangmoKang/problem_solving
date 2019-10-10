import sys
sys.stdin = open('input/2580.txt')


def check(r, c):
    global result
    if r == N:
        if result:
            return
        result = True
        for idx in range(N):
            print(*board[idx])
        print()
    else:
        if not result:
            if not board[r][c]:
                for num in range(1,N+1):
                    if not result:
                        if num not in garo[r] and num not in sero[c] and num not in nemo[3*(r//3)+(c//3)]:
                            garo[r].add(num)
                            sero[c].add(num)
                            nemo[3*(r//3)+(c//3)].add(num)
                            board[r][c] = num
                            if c == N - 1:
                                check(r + 1, 0)
                            else:
                                check(r, c + 1)
                            board[r][c] = 0
                            garo[r].remove(num)
                            sero[c].remove(num)
                            nemo[3*(r//3)+(c//3)].remove(num)
            else:
                if not result:
                    if c == N - 1:
                        check(r + 1, 0)
                    else:
                        check(r, c + 1)
            

N = 9
board = [list(map(int, input().split())) for _ in range(N)]

garo = [set() for _ in range(N)]
sero = [set() for _ in range(N)]
nemo = [set() for _ in range(N)]


for i in range(N):
    for j in range(N):
        if board[i][j]:
            if board[i][j] not in garo[i]:
                garo[i].add(board[i][j])
            if board[i][j] not in sero[j]:
                sero[j].add(board[i][j])

            for x in range(3):
                for y in range(3):
                    if 3*x <= i < 3*(x+1) and 3*y <= j < 3*(y+1):
                        if board[i][j] not in nemo[3*x+y]:
                            nemo[3*x+y].add(board[i][j])
                            break

result = False
check(0, 0)
