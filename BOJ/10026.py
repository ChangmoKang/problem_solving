import sys
sys.stdin = open('input/10026.txt')


def bfs(v, color):
    q = [v]
    while q:
        r, c = q.pop(0)
        for x in range(4):
            rr = r + dr[x]
            cc = c + dc[x]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and board[rr][cc] == color:
                visited[rr][cc] = 1
                q.append([rr, cc])
    return None


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
board = [list(input()) for _ in range(N)]

# R과 G를 같이봄
normal = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs([i, j], board[i][j])
            normal += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'

special = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs([i, j], board[i][j])
            special += 1

print(normal, special)
