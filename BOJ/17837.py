import sys
sys.stdin = open('input/17837.txt')


def move(r, c, d):
    rr, cc = r + dr[d], c + dc[d]
    b_rr, b_cc = r + dr[reverse[d]], c + dc[reverse[d]]

    if 0 <= rr < N and 0 <= cc < N:
        if board[rr][cc] == 2:
            if 0 <= b_rr < N and 0 <= b_cc < N:
                if board[b_rr][b_cc] == 2:
                    return r, c, reverse[d]
                else:
                    return b_rr, b_cc, reverse[d]
            else:
                return r, c, reverse[d]
        else:
            return rr, cc, d
    else:
        if board[b_rr][b_cc] == 2:
            return r, c, reverse[d]
        else:
            return b_rr, b_cc, reverse[d]


def init():
    for time in range(1, 1001):
        for horse_index in range(K):
            r, c, d = horse[horse_index]
            rr, cc, dd = move(r, c, d)

            horse[horse_index] = [rr, cc, dd]

            # 제자리에서 방향만 바뀌었다면 움직일 것이 없으므로 끝.
            if (r, c) == (rr, cc):
                continue
            
            if board[rr][cc] == 0:
                r_c_horse_index = horse_stack[r, c].index(horse_index)

                move_rr_cc_horses = horse_stack[r, c][r_c_horse_index:]
                horse_stack[r, c] = horse_stack[r, c][:r_c_horse_index]

                horse[move_rr_cc_horses[0]] = [rr, cc, dd]
                for tmp_horse_index in move_rr_cc_horses:
                    horse[tmp_horse_index] = [rr, cc, horse[tmp_horse_index][-1]]

                horse_stack[rr, cc].extend(move_rr_cc_horses)
                if len(horse_stack[rr, cc]) >= 4:
                    return time

            elif board[rr][cc] == 1:
                r_c_horse_index = horse_stack[r, c].index(horse_index)

                move_rr_cc_horses = horse_stack[r, c][r_c_horse_index:][::-1]
                horse_stack[r, c] = horse_stack[r, c][:r_c_horse_index]

                horse[move_rr_cc_horses[-1]] = [rr, cc, dd]
                for tmp_horse_index in move_rr_cc_horses:
                    horse[tmp_horse_index] = [rr, cc, horse[tmp_horse_index][-1]]

                horse_stack[rr, cc].extend(move_rr_cc_horses)
                if len(horse_stack[rr, cc]) >= 4:
                    return time
    return -1


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
reverse = {0: 1, 1: 0, 2: 3, 3: 2}

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

horse_stack = {(r, c): [] for r in range(N) for c in range(N)}
horse = []
for i in range(K):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    horse_stack[r, c].append(i)
    horse.append([r, c, d])

print(init())
