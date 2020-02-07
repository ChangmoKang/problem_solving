import sys
sys.stdin = open('input/18405.txt')


def bfs():
    time = 0
    while virus:
        for idx in sorted(virus.keys()):
            qs, virus[idx] = virus[idx], []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and not board[rr][cc]:
                        board[rr][cc] = idx
                        virus[idx].append([rr, cc])

            if not virus[idx]:
                virus.pop(idx)

        time += 1

        if board[R][C]:
            return board[R][C]

        if time == T:
            return board[R][C]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
T, R, C = map(int, input().split())
R -= 1
C -= 1

if board[R][C] or T == 0:
    print(board[R][C])
else:
    virus = {}
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                if board[i][j] not in virus:
                    virus[board[i][j]] = [[i, j]]
                else:
                    virus[board[i][j]].append([i, j])
    print(bfs())
