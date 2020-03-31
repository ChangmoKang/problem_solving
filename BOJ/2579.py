import sys
sys.stdin = open('input/2579.txt')
input = sys.stdin.readline


def solution():
    dp = [0]*N

    dp[0] = step[0]
    if N == 1:
        return dp[-1]

    dp[1] = step[0] + step[1]
    if N == 2:
        return dp[-1]
    
    dp[2] = max(step[0], step[1]) + step[2]
    for r in range(3, N):
        dp[r] = max(dp[r - 3] + step[r - 1] + step[r], dp[r - 2] + step[r])

    return dp[N - 1]


N = int(input())
step = [int(input()) for _ in range(N)]

print(solution())
