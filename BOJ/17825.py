import sys
sys.stdin = open('input/17825.txt')


def check(count, sub_result, targets):
    global result
    if count == 10:
        if sub_result > result:
            result = sub_result
    else:
        for move in range(1, 6):
            # 주사위가 있다면
            if turns[move]:
                turns[move] -= 1
                for target_index in range(4):
                    # 말이 도착점에 도착하지 않았다면
                    if targets[target_index] != [7, -1]:
                        copied_targets = [targets[w][:] for w in range(4)]
                        copied_sub_result = sub_result

                        r, c = copied_targets[target_index]

                        # 로직 시작
                        if r < 3:
                            if c + move == board_C[r] - 1:
                                r += 4
                                c = -1
                            elif c + move > board_C[r] - 1:
                                r += 1
                                c = c + move - board_C[r]
                            else:
                                c += move
                        else:
                            if c + move > board_C[r] - 1:
                                r = 7
                                c = -1
                            elif c + move == board_C[r] - 1:
                                c = board_C[r] - 1
                            else:
                                c += move

                        flag = 0
                        for x in range(4):
                            if x != target_index:
                                if [r, c] == copied_targets[x]:
                                    flag = 1

                        if not flag:
                            # 여기서부터 다시
                            # copied_sub_result += board[r][c]
                            check(count + 1, copied_sub_result, copied_targets)
                turns[move] += 1


# 주사위 저장
turns = [0]*6
for el in map(int, input().split()):
    turns[el] += 1

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
board_C = [len(board[x]) for x in range(len(board))]

# 말
TARGETS = [[0, -1] for _ in range(4)]

# 결과
result = 0

check(0, 0, TARGETS)
