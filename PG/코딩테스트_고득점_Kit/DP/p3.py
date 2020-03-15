def solution(triangle):
    N = len(triangle)
    dp = [[0]*(w + 1) for w in range(N)]
    dp[0][0] = triangle[0][0]

    for r in range(1, N):
        for c in range(len(dp[r])):
            if c - 1 >= 0:
                v = dp[r - 1][c - 1] + triangle[r][c]
                if v > dp[r][c]:
                    dp[r][c] = v
                    
            if c < len(dp[r - 1]):
                v = dp[r - 1][c] + triangle[r][c]
                if v > dp[r][c]:
                    dp[r][c] = v

    return max(dp[-1])


"""
>>> DP 리스트를 만들지 않고 풀이

def solution(triangle):
    N = len(triangle)

    for r in range(1, N):
        for c in range(len(triangle[r])):
            v = [0, 0]
            if c - 1 >= 0:
                v[0] = triangle[r - 1][c - 1]
                    
            if c < len(triangle[r - 1]):
                v [1] = triangle[r - 1][c]
                
            triangle[r][c] += max(v)

    return max(triangle[-1])
"""