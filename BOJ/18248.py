import sys
sys.stdin = open('input/18248.txt')


def check():
    for r in range(N):
        flag = 0
        for c in range(M):
            if order_board[r][c]:
                flag = 1
                break
        if flag:
            for j in range(c, M):
                if not order_board[r][j]:
                    return False
    return True


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
trans_board = list(map(list, zip(*board)))
j_axis_sum = [(i, sum(trans_board[i])) for i in range(M)]
j_axis_sum.sort(key=lambda x: x[1])

order_trans_board = []
for index, _ in j_axis_sum:
    order_trans_board.append(trans_board[index])

order_board = list(map(list, zip(*order_trans_board)))

print("YES") if check() else print("NO")
