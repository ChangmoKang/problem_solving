import sys
sys.stdin = open('input/17822.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
methods = [list(map(int, input().split())) for _ in range(K)]


visit_cnt = R * C
cnt_flag = 0
for x, d, k in methods:
    x_index = 1
    while True:
        board_index = x * x_index - 1
        if board_index > R - 1:
            break

        if d == 0:
            board[board_index] = board[board_index][-k:C] + board[board_index][:-k]
        else:
            board[board_index] = board[board_index][k:C] + board[board_index][:k]

        x_index += 1

    visited = [[0]*C for _ in range(R)]
    visite_flag = 0

    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                continue
            flag = 0
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if rr == -1 or rr == R:
                    continue

                if cc == -1:
                    cc = C - 1
                elif cc == C:
                    cc = 0

                if board[rr][cc] == board[r][c]:
                    flag = 1
                    visite_flag = 1
                    if not visited[rr][cc]:
                        visited[rr][cc] = 1
                        visit_cnt -= 1

            if flag and not visited[r][c]:
                visited[r][c] = 1
                visit_cnt -= 1

    if visit_cnt == 0:
        cnt_flag = 1
        break

    if visite_flag:
        for r in range(R):
            for c in range(C):
                if visited[r][c]:
                    board[r][c] = 0
    else:
        avg = sum([sum(board[x]) for x in range(R)]) / visit_cnt

        for r in range(R):
            for c in range(C):
                if board[r][c] == 0:
                    continue
                if board[r][c] > avg:
                    board[r][c] -= 1
                elif board[r][c] < avg:
                    board[r][c] += 1

print(sum([sum(board[x]) for x in range(R)])) if cnt_flag == 0 else print(0)
