import sys
sys.stdin = open('input/18404.txt')


def bfs():
    visited = [[0]*N for _ in range(N)]
    visited[night[0]][night[1]] = 1

    q = [night]
    move = 0
    while q:
        move += 1
        qs, q = q, []
        for r, c in qs:
            for x in range(8):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                    visited[rr][cc] = move
                    q.append([rr, cc])

    return [visited[i - 1][j - 1] for i, j in enemy]


dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]
N, M = map(int, input().split())
night = list(map(int, input().split()))
night[0] -= 1
night[1] -= 1

enemy = [list(map(int, input().split())) for _ in range(M)]
print(*bfs())
