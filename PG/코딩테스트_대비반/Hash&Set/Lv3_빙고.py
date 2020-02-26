def solution(board, nums):
    N = len(board)
    
    # 다 지운 경우 최댓값 리턴
    if len(nums) == N * N:
        return 2*N + 2
    
    nums = set(nums)

    row, col, diag = [0]*N, [0]*N, [0]*2

    for r in range(N):
        for c in range(N):
            if board[r][c] in nums:
                row[r] += 1
                col[c] += 1

                if r == c:
                    diag[0] += 1
                if r + c == N - 1:
                    diag[1] += 1

    return [*row, *col, *diag].count(N)