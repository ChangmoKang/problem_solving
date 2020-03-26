def solution(K, travel):
    dp = [[0]*(K + 1) for _ in range(len(travel))]
    
    dp[0][travel[0][0]] = travel[0][1]
    dp[0][travel[0][2]] = travel[0][3]

    for r in range(1, len(travel)):
        for k in range(K + 1):
            if dp[r - 1][k]:
                w_t, w_m, b_t, b_m = travel[r]
                
                if k + w_t <= K:
                    dp[r][k + w_t] = max(dp[r - 1][k] + w_m, dp[r][k + w_t])
                    
                if k + b_t <= K:
                    dp[r][k + b_t] = max(dp[r - 1][k] + b_m, dp[r][k + b_t])
                    
    return max(dp[r])
