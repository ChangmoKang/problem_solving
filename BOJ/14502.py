import sys
sys.stdin = open('input/14502.txt')


def check(r, c, count):
    global result
    if count == 3:
        c_board = [board[w][:] for w in range(R)]
        q = [virus[w][:] for w in range(len(virus))]
        sub_result = room
        while q:
            contents, q = q, []
            for r, c in contents:
                for x in range(4):
                    rr = r + dr[x]
                    cc = c + dc[x]
                    if 0 <= rr < R and 0 <= cc < C and not c_board[rr][cc]:
                        c_board[rr][cc] = 2
                        sub_result -= 1
                        q.append([rr, cc])
        if result < sub_result:
            result = sub_result
    else:
        while True:
            if c == C - 1:
                r += 1
                c = 0
            else:
                c += 1
            if r == R:
                break

            if board[r][c] == 0:
                board[r][c] = 1
                check(r, c, count + 1)
                board[r][c] = 0
                

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

virus = []
room = -3
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            room += 1
        elif board[i][j] == 2:
            virus.append([i, j])
result = 0

check(0, -1, 0)
print(result)
