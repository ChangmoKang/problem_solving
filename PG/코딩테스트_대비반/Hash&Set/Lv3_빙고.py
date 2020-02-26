def solution(board, nums):
    N = len(board)
    
    # 다 지운 경우 최댓값 리턴
    if len(nums) == N * N:
        return 2*N + 2
    
    nums = set(nums)

    row_bingo, col_bingo, diag_bingo = [0]*N, [0]*N, [0]*2

    for r, row in enumerate(board):
        for c, number in enumerate(row):
            if number in nums:
                row_bingo[r] += 1
                col_bingo[c] += 1

                if r == c:
                    diag_bingo[0] += 1
                if r + c == N - 1:
                    diag_bingo[1] += 1

    return [*row_bingo, *col_bingo, *diag_bingo].count(N)
