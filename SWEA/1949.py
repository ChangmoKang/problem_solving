import sys
sys.stdin = open('input/1949.txt')


def check(count, status, op):
    global result
    if count > result:
        result = count
    r = status[0]
    c = status[1]
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < N:
            if not visited[rr][cc]:
                visited[rr][cc] = 1
                if board[rr][cc] < board[r][c]:
                    check(count + 1, [rr, cc], op)
                else:
                    if op:
                        for k in range(1, K + 1):
                            board[rr][cc] -= k
                            if board[rr][cc] < board[r][c]:
                                check(count + 1, [rr, cc], 0)
                            board[rr][cc] += k
                visited[rr][cc] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_height = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > max_height:
                st = [[i, j]]
                max_height = board[i][j]
            elif board[i][j] == max_height:
                st.append([i, j])

    result = 0

    visited = [[0]*N for _ in range(N)]
    for s in st:
        visited[s[0]][s[1]] = 1
        check(1, s, 1)
        visited[s[0]][s[1]] = 0

    print(f"#{tc} {result}")
