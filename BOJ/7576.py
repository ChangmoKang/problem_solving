import sys
sys.stdin = open('input/7576.txt')


def bfs():
    global raw
    time = 0
    q = ripe
    while q and raw:
        time += 1
        contents, q = q, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and board[rr][cc] != -1 and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    raw -= 1
                    q.append([rr, cc])

    if raw:
        print(-1)
    else:
        print(time)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

raw = 0
ripe = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            raw += 1
        elif board[i][j] == 1:
            ripe.append([i, j])

if not raw:
    print(0)
else:
    visited = [[0]*C for _ in range(R)]
    for r, c in ripe:
        visited[r][c] = 1
    bfs()
