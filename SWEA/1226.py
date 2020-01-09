import sys
sys.stdin = open('input/1226.txt')


def find_start():
    for i in range(1, N -1):
        for j in range(1, N - 1):
            if board[i][j] == '2':
                return [i, j]


def bfs():
    visited = [[0]*N for _ in range(N)]
    visited[S[0]][S[1]] = 1

    q = [S]
    while q:
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < N and 0 <= cc < N and board[rr][cc] != '1' and not visited[rr][cc]:
                    if board[rr][cc] == '3':
                        return 1
                    visited[rr][cc] = 1
                    q.append([rr, cc])
    return 0


dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]
for _ in range(10):
    tc = int(input())
    N = 16
    board = [list(input()) for _ in range(N)]

    S = find_start()
    print(f"#{tc} {bfs()}")
