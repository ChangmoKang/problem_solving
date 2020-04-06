import sys
sys.stdin = open('input/1890.txt')


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if r == 0 and c == 0:
            dp[r][c] = 1
            continue
    
        for new_r in range(r - 1, -1, -1):
            if dp[new_r][c] and board[new_r][c] == r - new_r:
                dp[r][c] += dp[new_r][c]

        for new_c in range(c - 1, -1, -1):
            if dp[r][new_c] and board[r][new_c] == c - new_c:
                dp[r][c] += dp[r][new_c]

print(dp[-1][-1])
