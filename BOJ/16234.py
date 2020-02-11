import sys
sys.stdin = open('input/16234.txt')


def bfs():
    visited[i][j] = num
    q = [[i, j, board[i][j]]]

    cnt = 1
    total = board[i][j]

    while q:
        qs, q = q, []
        for r, c, population in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                    if L <= abs(population - board[rr][cc]) <= R:
                        visited[rr][cc] = num
                        total += board[rr][cc]
                        cnt += 1
                        q.append([rr, cc, board[rr][cc]])
    return int(total / cnt)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

t = 0
while True:
    num = 1
    visited = [[0]*N for _ in range(N)]
    s = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                s.append(bfs())
                num += 1
    
    for i in range(N):
        for j in range(N):
            board[i][j] = s[visited[i][j] - 1]
    
    if num == N*N + 1:
        break

    t += 1

print(t)
