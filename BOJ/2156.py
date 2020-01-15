import sys
sys.stdin = open('input/2156.txt')
input = sys.stdin.readline


N = int(input())
wine = [0] + [int(input()) for _ in range(N)]
if N <= 2:
    if N == 1:
        print(wine[1])
    else:
        print(wine[1] + wine[2])
else:
    dp = [0] * 10001
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    for r in range(3, N + 1):
        dp[r] = max(dp[r - 1], dp[r - 2] + wine[r], dp[r - 3] + wine[r - 1] + wine[r])

    print(dp[N])
