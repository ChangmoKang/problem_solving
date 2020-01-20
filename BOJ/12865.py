import sys
sys.stdin = open('input/12865.txt')


N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
bags.sort(key=lambda x: x[0])

# 1차원 dp
dp = [0]*(K + 1)
for W, V in bags:
    if W > K:
        break
    for i in range(K, W - 1, -1):
        test = V + dp[i - W]
        if test > dp[i]:
            dp[i] = test
            
print(dp[K])


# # 2차원 dp
# dp = [[0]*(K + 1) for _ in range(N + 1)]
# for i in range(N):
#     W, V = bags[i]
#     i += 1
#     for j in range(1, K + 1):
#         if W > j:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

# print(dp[N][K])
