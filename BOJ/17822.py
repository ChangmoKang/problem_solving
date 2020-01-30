import sys
sys.stdin = open('input/17822.txt')


spin = {0: -1, 1: 1}
N, M, T = map(int, input().split())
board = [[0]*M] + [list(map(int, input().split())) for _ in range(N)]
N += 1
methods = [list(map(int, input().split())) for _ in range(T)]


num = (N - 1) * M
value = sum([sum(board[index]) for index in range(1, N)])

for x, d, k in methods:
    if num == 0:
        break

    for i in range(x, N, x):
        board[i] = board[i][spin[d]*k:] + board[i][:spin[d]*k]

    delete_board = [[0]*M for _ in range(N)]
    big_flag = 0
    for i in range(1, N):
        for j in range(M):
            if board[i][j] != 0:
                flag = 0
                if j != M - 1:
                    if board[i][j - 1] != 0 and board[i][j - 1] == board[i][j]:
                        flag = 1
                        big_flag = 1
                        num -= 1
                        delete_board[i][j] = 1
                    elif board[i][j + 1] != 0 and board[i][j + 1] == board[i][j]:
                        flag = 1
                        big_flag = 1
                        num -= 1
                        delete_board[i][j] = 1
                else:
                    if board[i][j - 1] != 0 and board[i][j - 1] == board[i][j]:
                        flag = 1
                        big_flag = 1
                        num -= 1
                        delete_board[i][j] = 1
                    elif board[i][0] != 0 and board[i][0] == board[i][j]:
                        flag = 1
                        big_flag = 1
                        num -= 1
                        delete_board[i][j] = 1

                if not flag:
                    if 1 < i < N - 1:
                        if board[i - 1][j] != 0 and board[i - 1][j] == board[i][j]:
                            big_flag = 1
                            num -= 1
                            delete_board[i][j] = 1
                        elif board[i + 1][j] != 0 and board[i + 1][j] == board[i][j]:
                            big_flag = 1
                            num -= 1
                            delete_board[i][j] = 1
                    elif i == 1:
                        if board[i + 1][j] != 0 and board[i + 1][j] == board[i][j]:
                            big_flag = 1
                            num -= 1
                            delete_board[i][j] = 1
                    elif i == N - 1:
                        if board[i - 1][j] != 0 and board[i - 1][j] == board[i][j]:
                            big_flag = 1
                            num -= 1
                            delete_board[i][j] = 1

    if not big_flag:
        avg = value / num

        for i in range(1, N):
            for j in range(M):
                if board[i][j] != 0:
                    if board[i][j] > avg:
                        board[i][j] -= 1
                        value -= 1
                    elif board[i][j] < avg:
                        board[i][j] += 1
                        value += 1
    else:
        for i in range(1, N):
            for j in range(M):
                if delete_board[i][j]:
                    value -= board[i][j]
                    board[i][j] = 0

print(value)
