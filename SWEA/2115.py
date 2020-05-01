import sys
sys.stdin = open('input/2115.txt')


def calc(r, c):
    max_pow_honey = 0
    for i in range(1, 1 << M):
        temp_honey = 0
        temp_pow_honey = 0
        for j in range(M):
            if i & 1 << j:
                temp_honey += board[r][c + j]
                temp_pow_honey += pow_board[r][c + j]
        
        if temp_honey <= C and temp_pow_honey > max_pow_honey:
            max_pow_honey = temp_pow_honey

    return max_pow_honey


def check(r, c, count, honey):
    global answer
    if count == 2:
        if honey > answer:
            answer = honey
        return

    while True:
        if r == N:
            break

        if c + M <= N:
            if sum(board[r][c:c+M]) <= C:
                check(r, c + M, count + 1, honey + sum(pow_board[r][c:c+M]))
            else:
                check(r, c + M, count + 1, honey + calc(r, c))
        
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
    check(0, 0, 0, 0)
    print(f"#{tc} {answer}")
