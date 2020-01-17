import sys
sys.stdin = open('input/1912.txt')


N = int(input())
a = list(map(int, input().split()))
dp = [0]*N
dp[0] = a[0]

s = a[0]
for i in range(1, N):
    if s >= 0 and a[i] >= 0:
        s += a[i]
        dp[i] = s
    elif s >= 0 and a[i] < 0:
        s += a[i]
        dp[i] = s
        if s < 0:
            s = 0
    elif s < 0:
        s = a[i]
        dp[i] = s

print(max(dp))
