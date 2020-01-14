import sys
sys.stdin = open('input/2579.txt')
input = sys.stdin.readline


N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [0]*N
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0], stairs[1]) + stairs[2]

for r in range(3, N):
    dp[r] = max(dp[r - 3] + stairs[r - 1] + stairs[r], dp[r - 2] + stairs[r])

print(dp[N - 1])
