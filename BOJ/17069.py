import sys
sys.stdin = open('input/17069.txt')


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
for r in range(N):
    for c in range(1, N):
        if c < N - 1 and not board[r][c + 1]:
            dp[r][c + 1][0] += dp[r][c][0] + dp[r][c][2]
        if r < N - 1 and not board[r + 1][c]:
            dp[r + 1][c][1] += dp[r][c][1] + dp[r][c][2]
        if r < N - 1 and c < N - 1 and not (board[r][c + 1] or board[r + 1][c] or board[r + 1][c + 1]):
            dp[r + 1][c + 1][2] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]
print(sum(dp[N - 1][N - 1]))
