import sys
sys.stdin = open('input/15558.txt')


def bfs():
    dr = [0, 0, -1]
    dc = [1, -1, K]
    visited = [[0]*N for _ in range(2)]
    visited[0][0] = 1
    q = [[0, 0]]

    status = 0
    while q:
        status += 1
        qs, q = q, []
        for r, c in qs:
            for x in range(3):
                rr, cc = abs(r + dr[x]), c + dc[x]
                if cc >= N:
                    return 1
                if status <= cc < N and board[rr][cc] and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    q.append([rr, cc])
    return 0


N, K = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(2)]
print(bfs())
