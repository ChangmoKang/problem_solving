import sys
sys.stdin = open('input/2293.txt')

N, target = map(int, input().split())
dp = [1] + [0]*target

for _ in range(N):
    kind = int(input())

    if kind > target:
        continue

    for i in range(kind, target + 1):
        dp[i] += dp[i - kind]

print(dp[-1])
