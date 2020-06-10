import sys
sys.stdin = open('input/19236.txt')


def check(o_board, o_fish, o_shark):
    global answer

    s_r, s_c, result, s_d = o_shark

    if not o_fish or not shark_in_board(s_r, s_c):
        if result > answer:
            answer = result
        return
      
    for index in sorted(o_fish):
        r, c, d = o_fish[index]

        for x in range(d, d + 8):
            x %= 8
            rr, cc = r + dr[x], c + dc[x]
            if 0 <= rr < N and 0 <= cc < N and o_board[rr][cc] != SHARK:
                if o_board[rr][cc] == EMPTY:
                    o_board[r][c] = EMPTY
                    o_board[rr][cc] = index
                    o_fish[index] = [rr, cc, x]
                    break

                other_index = o_board[rr][cc]
                _, _, dd = o_fish[other_index]

                o_fish[other_index] = [r, c, dd]
                o_board[r][c] = other_index
                o_fish[index] = [rr, cc, x]
                o_board[rr][cc] = index
                break

    cnt = 0
    while True:
        cnt += 1

        s_rr = s_r + dr[s_d]*cnt
        s_cc = s_c + dc[s_d]*cnt

        if not shark_in_board(s_rr, s_cc):
            check(o_board, o_fish, (s_rr, s_cc, result, s_d))
            break

        if o_board[s_rr][s_cc] == EMPTY:
            continue


        temp = o_board[s_rr][s_cc]
        t_r, t_c, t_d = o_fish[temp]

        o_board[s_r][s_c] = EMPTY
        o_board[s_rr][s_cc] = SHARK
        o_fish.pop(temp)
        n_board = [o_b[:] for o_b in o_board]
        n_fish = {key: value[:] for key, value in o_fish.items()}
        check(n_board, n_fish, (s_rr, s_cc, result + temp, t_d))
        o_fish[temp] = (t_r, t_c, t_d)
        o_board[s_rr][s_cc] = temp
        o_board[s_r][s_c] = SHARK


def shark_in_board(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

N = 4
R, C, D = range(3)
EMPTY, SHARK = 0, 17
board = [[EMPTY]*N for _ in range(N)]
fish = {}
for r in range(N):
    temp = list(map(int, input().split()))
    for c in range(N):
        index, dir = temp[2*c: 2*c + 2]
        dir -= 1

        if r == 0 and c == 0:
            shark = (r, c, index, dir)
            board[r][c] = SHARK
            continue

        fish[index] = [r, c, dir]
        board[r][c] = index

answer = 0
check(board, fish, shark)
print(answer)