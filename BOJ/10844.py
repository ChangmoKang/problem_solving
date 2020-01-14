import sys
sys.stdin = open('input/10844.txt')


N = int(input())
dp = [[0]*11 for _ in range(N + 1)]

for c in range(1, 10):
    dp[1][c] = 1

for r in range(2, N + 1):
    for c in range(10):
        if c == 0:
            dp[r][c] = dp[r - 1][c + 1] % 1000000000
        elif c == 9:
            dp[r][c] = dp[r - 1][c - 1] % 1000000000
        else:
            dp[r][c] = (dp[r - 1][c + 1] + dp[r - 1][c - 1])  % 1000000000

print(sum(dp[N]) % 1000000000)
