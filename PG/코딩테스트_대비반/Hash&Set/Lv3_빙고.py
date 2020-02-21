def solution(board, nums):
    N = len(board)
    
    # 다 지운 경우 최댓값 리턴
    if len(nums) == N * N:
        return 2*N + 2
    
    num_to_coord = {board[r][c]: (r, c) for r in range(N) for c in range(N)}
    
    checked_board = [[False]*N for _ in range(N)]

    for num in nums:
        r, c = num_to_coord[num]
        checked_board[r][c] = True
    
    answer = 0
    
    # 가로방향 검색
    for r in range(N):
        for c in range(N):
            if not checked_board[r][c]:
                break
        else:
            answer += 1
            
    # 세로방향 검색
    for c in range(N):
        for r in range(N):
            if not checked_board[r][c]:
                break
        else:
            answer += 1
            
    # 대각선 방향 검색
    for r in range(N):
        if not checked_board[r][r]:
            break
    else:
        answer += 1

    # 대각선 방향 검색
    for r in range(N):
        if not checked_board[r][(N - 1) - r]:
            break
    else:
        answer += 1
    
    return answer
