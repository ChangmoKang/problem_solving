from collections import Counter, defaultdict

def solution(board, nums):
    N = len(board)
    
    # 다 지운 경우 최댓값 리턴
    if len(nums) == N * N:
        return 2*N + 2
    
    num_to_coord = {board[r][c]: (r, c) for r in range(N) for c in range(N)}

    bingo = defaultdict(int)
    
    for num in nums:
        r, c = num_to_coord[num]
        bingo[f"r{r}"] += 1
        bingo[f"c{c}"] += 1
        
        if r == c:
            bingo["d0"] += 1
        if c == N - 1 - r:
            bingo["d1"] += 1
            
    return Counter(bingo.values()).get(N, 0)
