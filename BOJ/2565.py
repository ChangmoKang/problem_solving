import sys
sys.stdin = open('input/2565.txt')


N = int(input())
con = [list(map(int, input().split())) for _ in range(N)]
con.sort()
con = [con[i][1] for i in range(N)]

dp = [0]*N
dp[0] = 1

for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if con[i] > con[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
        elif con[i] == con[j]:
            dp[i] = dp[j]

print(N - max(dp))
