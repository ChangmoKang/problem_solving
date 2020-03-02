import sys
sys.stdin = open('input/1949.txt')


def check(r, c, x, sub_result):
    global result

    if sub_result > result:
        result = sub_result

    for dr, dc in DELTAS:
        rr, cc = r + dr, c + dc
        if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
            visited[rr][cc] = 1
            if board[r][c] > board[rr][cc]:
                check(rr, cc, x, sub_result + 1)
            else:
                if x:
                    for k in range(1, K + 1):
                        if board[r][c] > board[rr][cc] - k:
                            board[rr][cc] -= k
                            check(rr, cc, 0, sub_result + 1)
                            board[rr][cc] += k
            visited[rr][cc] = 0


DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    max_height = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > max_value:
                max_height = [[i, j]]
                max_value = board[i][j]
            elif board[i][j] == max_value:
                max_height.append([i, j])
    
    result = 0
    for i, j in max_height:
        visited = [[0]*N for _ in range(N)]
        visited[i][j] = 1
        check(i, j, 1, 1)
    
    print("#{} {}".format(tc, result))
