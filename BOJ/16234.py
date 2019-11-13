import sys
sys.stdin = open('input/16234.txt')


def bfs(init):
    save = [init]
    q = [init]
    while q:
        r, c = q.pop(0)
        for x in range(4):
            rr = r + dr[x]
            cc = c + dc[x]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and L <= abs(board[r][c] - board[rr][cc]) <= R:
                visited[rr][cc] = number
                save.append([rr, cc])
                q.append([rr, cc])
    if len(save) > 1:
        union = int(sum([board[s[0]][s[1]] for s in save])/len(save))
        for r, c in save:
            board[r][c] = union


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


result = 0
while True:
    visited = [[0]*N for _ in range(N)]
    number = 1
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = number
                bfs([i, j])
                number += 1
    if number == N ** 2 + 1:
        break

    result += 1

print(result)
