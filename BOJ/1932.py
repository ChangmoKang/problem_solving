import sys
sys.stdin = open('input/1932.txt')
input = sys.stdin.readline


N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(i + 1) for i in range(N)]

for c in range(N):
    dp[N - 1][c] = triangle[N - 1][c]

for r in range(N - 2, -1, -1):
    for c in range(r + 1):
        dp[r][c] = max(dp[r + 1][c], dp[r + 1][c + 1]) + triangle[r][c]

print(dp[0][0])
