import sys
sys.stdin = open('input/3187.txt')
input = sys.stdin.readline


def bfs(r, c):
    global sheep, wolf
    k = 0
    v = 0
    if board[r][c] == 'k':
        k += 1
    elif board[r][c] == 'v':
        v += 1
    visited[r][c] = 1
    q = [[r, c]]
    while q:
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and board[rr][cc] != '#' and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    if board[rr][cc] == 'k':
                        k += 1
                    elif board[rr][cc] == 'v':
                        v += 1
                    q.append([rr, cc])
    if k > v:
        sheep += k
    else:
        wolf += v


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [input() for _ in range(R)]

sheep, wolf = 0, 0
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and not visited[i][j]:
            bfs(i, j)

print(sheep, wolf)
