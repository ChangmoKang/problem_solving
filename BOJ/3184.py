import sys
sys.stdin = open('input/3184.txt')


def bfs(v):
    global result_sheep, result_wolf
    sheep = 0
    wolf = 0
    if board[v[0]][v[1]] == 'o':
        sheep += 1
    elif board[v[0]][v[1]] == 'v':
        wolf += 1
    q = [v]
    while q:
        r, c = q.pop(0)
        for x in range(4):
            rr = r + dr[x]
            cc = c + dc[x]
            if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and board[rr][cc] != '#':
                visited[rr][cc] = 1
                if board[rr][cc] == 'o':
                    sheep += 1
                elif board[rr][cc] == 'v':
                    wolf += 1
                q.append([rr, cc])
    if sheep > wolf:
        result_sheep += sheep
    else:
        result_wolf += wolf


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

result_sheep = 0
result_wolf = 0
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j] != '#':
            visited[i][j] = 1
            bfs([i, j])

print(result_sheep, result_wolf)
