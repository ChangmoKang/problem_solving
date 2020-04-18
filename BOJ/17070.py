import sys
sys.stdin = open('input/17070.txt')


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for r in range(N):
    for c in range(1, N):
        if board[r][c]:
            continue

        dp[r][c][0] += (dp[r][c - 1][0] + dp[r][c - 1][2])
        dp[r][c][1] += (dp[r - 1][c][1] + dp[r - 1][c][2])

        if not board[r - 1][c] and not board[r][c - 1]:
            dp[r][c][2] += sum(dp[r - 1][c - 1])

print(sum(dp[-1][-1]))
