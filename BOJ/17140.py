import sys
sys.stdin = open('input/17140.txt')


def check():
    global board

    if R < 3 and C < 3 and board[R][C] == K:
        return 0

    for t in range(1, 101):
        flag = 0
        N_R = len(board)
        N_C = len(board[0])

        # 열의 길이가 길다면 transpose
        if N_R < N_C:
            N_R, N_C = N_C, N_R
            board = list(map(list, zip(*board)))
            flag = 1

        max_N = 0
        for i in range(N_R):
            dic = {}
            for j in range(N_C):
                if board[i][j]:
                    if board[i][j] not in dic:
                        dic[board[i][j]] = 1
                    else:
                        dic[board[i][j]] += 1
            i_board = []
            for a, b in sorted(dic.items(), key=lambda x: (x[1], x[0])):
                i_board.append(a)
                i_board.append(b)

                if len(i_board) == 100:
                    break

            if len(i_board) > max_N:
                max_N = len(i_board)

            board[i] = i_board
        
        # 0 채워 넣기
        for i in range(N_R):
            board[i].extend([0]*(max_N - len(board[i])))

        # 열의 길이가 더 길었더라면 다시 board를 transpose
        if flag:
            board = list(map(list, zip(*board)))

        if R < len(board) and C < len(board[0]) and board[R][C] == K:
            return t

    return -1


N = 3
R, C, K = map(int, input().split())
R -= 1
C -= 1
board = [list(map(int, input().split())) for _ in range(N)]

print(check())
