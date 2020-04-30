import sys
sys.stdin = open('input/2115.txt')


def calc(r, c, sub_count, sub_result, sub_pow_result):
    global tmp
    if sub_count == M - 1:
        return

    for i in range(M):
        if not visited[i]:
            visited[i] = True
            if sub_result + board[r][c + i] <= C:
                if sub_pow_result + pow_board[r][c + i] > tmp:
                    tmp = sub_pow_result + pow_board[r][c + i]
                calc(r, c, sub_count + 1, sub_result + board[r][c + i], sub_pow_result + pow_board[r][c + i])
            visited[i] = False


def check(r, c, count, result):
    global tmp, answer
    if count == 2:
        if result > answer:
            answer = result
        return

    while True:
        if r == N:
            break

        if c + M <= N:
            if sum(board[r][c:c+M]) <= C:
                check(r, c + M, count + 1, result + sum(pow_board[r][c:c+M]))
            else:
                tmp = 0
                calc(r, c, 0, 0, 0)
                check(r, c + M, count + 1, result + tmp)
        
        if c >= N - 1:
            r += 1
            c = 0
        else:
            c += 1


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    pow_board = [[pow(board[r][c], 2) for c in range(N)] for r in range(N)]

    answer = 0
    visited = [False]*M
    check(0, 0, 0, 0)
    print(f"#{tc} {answer}")
