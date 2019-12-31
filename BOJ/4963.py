import sys
sys.stdin = open('input/4963.txt')


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
while True:
    C, R = map(int, input().split())
    if R == 0 and C == 0:
        break
    board = [list(map(int, input().split())) for _ in range(R)]
    visited = [[0]*C for _ in range(R)]

    island_cnt = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] and not visited[i][j]:
                island_cnt += 1
                visited[i][j] = 1
                q = [[i, j]]
                while q:
                    qs, q, = q, []
                    for r, c in qs:
                        for x in range(8):
                            rr, cc = r + dr[x], c + dc[x]
                            if 0 <= rr < R and 0 <= cc < C and board[rr][cc] and not visited[rr][cc]:
                                visited[rr][cc] = 1
                                q.append([rr, cc])
    print(island_cnt)
