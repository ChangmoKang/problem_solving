import sys
sys.stdin = open('input/18427.txt')


N, M, H = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(H + 1)
dp[0] = 1

for student_i in range(N):
    for target_h in range(H, 0, -1):
        for block_h in block[student_i]:
            if 0 < block_h <= target_h:
                dp[target_h] += dp[target_h - block_h]
        
        dp[target_h] %= 10007

print(dp[-1])
