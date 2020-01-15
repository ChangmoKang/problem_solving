import sys
sys.stdin = open('input/11053.txt')


N = int(input())
a = [0] + list(map(int, input().split()))
dp = [0]*(N + 1)
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if a[i] > a[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
        elif a[i] == a[j]:
            dp[i] == dp[j]

print(max(dp))
