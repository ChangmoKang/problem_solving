import sys
sys.stdin = open('input/1868.txt')


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    unknown = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                unknown += 1

                cnt = 0
                for x in range(8):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and board[rr][cc] == '*':
                        cnt += 1
                board[r][c] = cnt

    visited = [[0]*N for _ in range(N)]
    click = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not visited[i][j]:
                click += 1

                visited[i][j] = 1
                unknown -= 1
                q = [[i, j]]

                while q:
                    qs, q = q, []
                    for r, c in qs:
                        for x in range(8):
                            rr, cc = r + dr[x], c + dc[x]
                            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and board[rr][cc] != '*':
                                visited[rr][cc] = 1
                                unknown -= 1
                                if board[rr][cc] == 0:
                                    q.append([rr, cc])

    print(f"#{tc} {click + unknown}")
