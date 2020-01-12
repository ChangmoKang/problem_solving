import sys
sys.stdin = open('input/1149.txt')
input = sys.stdin.readline


N = int(input())
cost = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][2], dp[i - 1][0]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

print(min(dp[N]))
