import sys
sys.stdin = open('input/7569.txt')


def bfs(q):
    global time, remain
    visited = [[[0]*C for _ in range(R)] for _ in range(H)]
    for h, r, c in q:
        visited[h][r][c] = 1
    while q:
        contents, q = q, []
        for h, r, c in contents:
            for d in range(6):
                hh = h + dh[d]
                rr = r + dr[d]
                cc = c + dc[d]
                if 0 <= hh < H and 0 <= rr < R and 0 <= cc < C and not visited[hh][rr][cc]:
                    visited[hh][rr][cc] = 1
                    if board[hh][rr][cc] == 0:
                        remain -= 1
                        q.append([hh, rr, cc])
        time += 1
    time -= 1

dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]
C, R, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]

remain = 0
q = []
for h in range(H):
    for r in range(R):
        for c in range(C):
            if board[h][r][c] == 0:
                remain += 1
            elif board[h][r][c] == 1:
                q.append([h, r, c])

if remain == 0:
    print(0)
elif not q:
    print(-1)
else:
    time = 0
    bfs(q)
    if remain:
        print(-1)
    else:
        print(time)