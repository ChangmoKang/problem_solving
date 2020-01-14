import sys
sys.stdin = open('input/1463.txt')


N = int(input())
if N == 1:
    print(0)
else:
    dp = [0]*(N + 1)
    dp[2] = 1

    for r in range(3, N + 1):
        if r % 6 == 0:
            dp[r] = min(dp[r//3], dp[r//2], dp[r - 1]) + 1
        elif r % 3 == 0:
            dp[r] = min(dp[r//3], dp[r - 1]) + 1
        elif r % 2 == 0:
            dp[r] = min(dp[r//2], dp[r - 1]) + 1
        else:
            dp[r] = dp[r - 1] + 1

    print(dp[N])
