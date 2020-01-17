import sys
sys.stdin = open('input/9251.txt')

A = input()
N_A = len(A)
B = input()
N_B = len(B)

dp = [[0]*(N_B + 1) for _ in range(N_A + 1)]
result = -1
for a_index in range(1, N_A + 1):
    for b_index in range(1, N_B + 1):
        if A[a_index - 1] == B[b_index - 1]:
            dp[a_index][b_index] = dp[a_index - 1][b_index - 1] + 1
        else:
            dp[a_index][b_index] = max(dp[a_index][b_index - 1], dp[a_index - 1][b_index])

        if dp[a_index][b_index] > result:
            result = dp[a_index][b_index]

print(result)
