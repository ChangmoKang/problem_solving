import sys
sys.stdin = open('input/11722.txt')


N = int(input())
nums = list(map(int, input().split()))
dp = [1]*N

for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if nums[i] > nums[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
        elif nums[i] == nums[j]:
            dp[i] == dp[j]

print(max(dp))
