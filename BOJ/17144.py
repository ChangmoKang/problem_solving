import sys
sys.stdin = open('input/17144.txt')


def find_robot():
    for r in range(R):
        if board[r][0] == -1:
            return r


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ccw = [3, 0, 2, 1]
cw = [3, 1, 2, 0]
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
robot = find_robot()

for _ in range(T):
    # 확산
    spread = {}
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                big_flag = 1

            if board[i][j] >= 5:
                cnt = 0
                for x in range(4):
                    ii, jj = i + dr[x], j + dc[x]
                    if 0 <= ii < R and 0 <= jj < C and (ii, jj) != (robot, 0) and (ii, jj) != (robot + 1, 0):
                        if (ii, jj) not in spread:
                            spread[ii, jj] = int(board[i][j]/5)
                        else:
                            spread[ii, jj] += int(board[i][j]/5)

                        cnt += 1

                if cnt:
                    if (i, j) not in spread:
                        spread[i, j] = -cnt * int(board[i][j]/5)
                    else:
                        spread[i, j] -= cnt * int(board[i][j]/5)

    for key, value in spread.items():
        board[key[0]][key[1]] += value

    # 공기청정기 위쪽 시계 반대방향
    r, c = robot, 0
    tmp1 = 0
    tmp2 = None
    for d in ccw:
        while True:
            rr, cc = r + dr[d], c + dc[d]
            if 0 <= rr < R and 0 <= cc < C:
                if board[rr][cc] == - 1:
                    break

                if tmp1 is not None:
                    tmp2 = board[rr][cc]
                    board[rr][cc] = tmp1
                    tmp1 = None
                else:
                    tmp1 = board[rr][cc]
                    board[rr][cc] = tmp2
                    tmp2 = None
                
                r, c = rr, cc
            else:
                break

    # 공기청정기 아래쪽 시계 방향
    r, c = robot + 1, 0
    tmp1 = 0
    tmp2 = None
    for d in cw:
        while True:
            rr, cc = r + dr[d], c + dc[d]
            if 0 <= rr < R and 0 <= cc < C:
                if board[rr][cc] == - 1:
                    break

                if tmp1 is not None:
                    tmp2 = board[rr][cc]
                    board[rr][cc] = tmp1
                    tmp1 = None
                else:
                    tmp1 = board[rr][cc]
                    board[rr][cc] = tmp2
                    tmp2 = None
                
                r, c = rr, cc
            else:
                break

print(sum([board[i][j] for i in range(R) for j in range(C) if board[i][j] > 0]))
