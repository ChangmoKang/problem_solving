DIVISOR = 1_000_000_007
def solution(n, money):
    dp = [0]*(n + 1)
    
    dp[0] = 1
    for i in range(money[0], n + 1, money[0]):
        dp[i] = 1
        
    for i in range(1, len(money)):
        for j in range(money[i], n + 1):
            dp[j] += dp[j - money[i]] % DIVISOR

    return dp[n]
