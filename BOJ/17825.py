import sys
sys.stdin = open('input/17825.txt')


def check(count, sub_result):
    global result
    if count == 10:
        if sub_result > result:
            result = sub_result
    else:
        move = TURNS[count]
        for target_index in range(4):
            if TARGETS[target_index] != [7, -1]:
                copied_sub_result = sub_result

                r, c = TARGETS[target_index]

                if r < 3:
                    if c + move > end_index[r]:
                        rr = r + 1
                        cc = c + move - end_index[r] - 1
                        copied_sub_result += board[rr][cc]
                    elif c + move == end_index[r]:
                        rr = r
                        cc = end_index[r]
                        copied_sub_result += board[rr][cc]
                        rr += 4
                        cc = -1
                    else:
                        rr = r
                        cc = c + move
                        copied_sub_result += board[rr][cc]
                else:
                    if c + move > end_index[r]:
                        rr = 7
                        cc = -1
                    elif c + move == end_index[r]:
                        rr = r
                        cc = end_index[r]
                        copied_sub_result += board[rr][cc]
                    else:
                        rr = r
                        cc = c + move
                        copied_sub_result += board[rr][cc]

                flag = 0
                for x in range(4):
                    if x != target_index:
                        if [rr, cc] == TARGETS[x] and [7, -1] != TARGETS[x] and [0, -1] != TARGETS[x]:
                            flag = 1
                            break
                        elif 3 <= rr <= 6 and end_index[rr] == cc:
                            if 3 <= TARGETS[x][0] <= 6 and end_index[TARGETS[x][0]] == TARGETS[x][1]:
                                flag = 1
                                break
                        elif 4 <= rr <= 6 and -4 <= cc - (end_index[rr] + 1) <= -2:
                            if 4 <= TARGETS[x][0] <= 6 and -4 <= TARGETS[x][1] - (end_index[TARGETS[x][0]] + 1) <= -2 and cc - (end_index[rr] + 1) == TARGETS[x][1] - (end_index[TARGETS[x][0]] + 1):
                                flag = 1
                                break

                if not flag:
                    TARGETS[target_index] = [rr, cc]
                    check(count + 1, copied_sub_result)
                    TARGETS[target_index] = [r, c]


# 주사위 저장
TURNS = list(map(int, input().split()))

# 판
board = [
    [2, 4, 6, 8, 10],
    [12, 14, 16, 18, 20],
    [22, 24, 26, 28, 30],
    [32, 34, 36, 38, 40],
    [13, 16, 19, 25, 30, 35, 40],
    [22, 24, 25, 30, 35, 40],
    [28, 27, 26, 25, 30, 35, 40]
]

end_index = [len(board[x]) - 1 for x in range(len(board))]

# 말
TARGETS = [[0, -1] for _ in range(4)]

# 결과
result = 0

check(0, 0)
print(result)
