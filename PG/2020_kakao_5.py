## Input
N = 5
# targets = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
targets = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

## 시작
N += 1

# 기둥
g_board = [[-1]*N for _ in range(N)]
# 보
b_board = [[-1]*N for _ in range(N)]

for c, r, kind, method in targets:
    rr = (N - 1) - r
    cc = c
    # method가 '설치'인 경우
    if method:
        # kind가 '보'인 경우
        if kind:
            if (rr + 1 < N and g_board[rr + 1][cc] == 0) or (rr + 1 < N and cc + 1 < N and g_board[rr + 1][cc + 1] == 0) or ((cc - 1 >= 0 and b_board[rr][cc - 1] == 1) and (cc + 1 < N and b_board[rr][cc + 1] == 1)):
                b_board[rr][cc] = 1
        # kind가 '기둥'인 경우
        else:
            # 바닥이거나 밑이 기둥이거나 보가 설치되어 있을 경우 설치
            if rr == (N - 1) or (rr + 1 < N and g_board[rr + 1][cc] == 0) or (cc - 1 >= 0 and b_board[rr][cc - 1] == 1) or b_board[rr][cc] == 1:
                g_board[rr][cc] = 0
    # method가 '삭제'인 경우
    else:
        if kind:
            flag = 1
            if g_board[rr][cc] == 0:
                if (rr + 1 < N and g_board[rr + 1][cc] == 0) or (cc - 1 >= 0 and rr + 1 < N and b_board[rr][cc - 1] == 1 and g_board[rr + 1][cc - 1] == 0):
                    pass
                else:
                    flag = 0
            if cc + 1 < N and g_board[rr][cc + 1] == 0:
                if (rr + 1 < N and g_board[rr + 1][cc + 1] == 0) or (cc + 2 < N and rr + 1 < N and b_board[rr][cc + 1] == 1 and g_board[rr + 1][cc + 2] == 0):
                    pass
                else:
                    flag = 0
            if cc - 1 >= 0 and b_board[rr][cc - 1] == 1:
                if rr + 1 < N and (g_board[rr + 1][cc - 1] == 0 or g_board[rr + 1][cc] == 0):
                    pass
                else:
                    flag = 0
            if cc + 1 < N and b_board[rr][cc + 1] == 1:
                if rr + 1 < N and cc + 2 < N and (g_board[rr + 1][cc + 1] == 0 or g_board[rr + 1][cc + 2] == 0):
                    pass
                else:
                    flag = 0

            if flag:
                b_board[rr][cc] = -1
        else:
            flag = 1
            if g_board[rr - 1][cc] == 0:
                if (cc - 1 >= 0 and g_board[rr][cc - 1] == 0 and b_board[rr - 1][cc - 1] == 1) or (cc + 1 < N and g_board[rr][cc + 1] == 0 and b_board[rr - 1][cc] == 1) or (cc - 2 >= 0 and cc + 1 < N and b_board[rr - 1][cc - 2] == 1 and b_board[rr - 1][cc - 1] == 1 and b_board[rr - 1][cc] == 1  and b_board[rr - 1][cc + 1] == 1):
                    pass
                else:
                    flag = 0
            if cc - 1 >= 0 and b_board[rr - 1][cc - 1] == 1:
                if g_board[rr][cc - 1] == 0 or ((cc - 2 >= 0 and b_board[rr - 1][cc - 2] == 1) and b_board[rr - 1][cc] == 1):
                    pass
                else:
                    flag = 0
            if b_board[rr - 1][cc] == 1:
                if (cc + 1 < N and g_board[rr][cc + 1] == 0) or ((cc - 1 >= 0 and b_board[rr - 1][cc - 1] == 1) and (cc + 1 < N and b_board[rr - 1][cc + 1] == 1)):
                    pass
                else:
                    flag = 0

            if flag:
                g_board[rr][cc] = -1

result = []
for r in range(N):
    for c in range(N):
        if g_board[r][c] == 0:
            result.append([c, (N - 1) - r, 0])
        if b_board[r][c] == 1:
            result.append([c, (N - 1) - r, 1])
result.sort()
print(result)