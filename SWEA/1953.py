import sys
sys.stdin = open('input/1953.txt')


def check(position):
    global result

    t = 1
    q = [position]
    while q and t < T:
        contents, q = q, []
        for content in contents:
            for i in ways[content[2]]:
                r = content[0] + dr[i]
                c = content[1] + dc[i]
                if 0 <= r < N and 0 <= c < M and board[r][c] in possible[i]:
                    if not visited[r][c]:
                        visited[r][c] = 1
                        result += 1
                        q.append([r, c, board[r][c]])
        t += 1
    return 0


ways = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}

possible = {
    0: [1, 2, 5, 6],
    1: [1, 2, 4, 7],
    2: [1, 3, 4, 5],
    3: [1, 3, 6, 7]
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N, M, R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1

    result = 1

    check([R, C, board[R][C]])
    print(f"#{tc} {result}")
