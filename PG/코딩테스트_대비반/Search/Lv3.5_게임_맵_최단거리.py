def solution(maps):
    FROM_START, FROM_END = 0, 1
    ROUTE = 1
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    N, M = len(maps), len(maps[0])
    
    visited = [[None]*M for _ in range(N)]
    visited[0][0] = (1, FROM_START)
    visited[N - 1][M - 1] = (1, FROM_END)
    
    q = [[0, 0, FROM_START], [N - 1, M - 1, FROM_END]]
    while q:
        flag = [False]*2

        target_same_depth_q , q = q, [] # 같은 depth를 조사하기 위함 >> 이렇게 해야 위의 flag가 의미가 있음
        
        for r, c, k in target_same_depth_q:
            for dr, dc in DELTAS:
                next_r, next_c = r + dr, c + dc
                if 0 <= next_r < N and 0 <= next_c < M and maps[next_r][next_c] == ROUTE:
                    if visited[next_r][next_c] is not None:
                        if visited[next_r][next_c][-1] != k:
                            return visited[next_r][next_c][0] + visited[r][c][0]
                    else:
                        flag[k] = True # 길이 있는 경우
                        visited[next_r][next_c] = (visited[r][c][0] + 1, k)
                        q.append([next_r, next_c, k])
        
        if flag != [True]*2: # 한쪽 이상에서 길이 막힌 경우 -1 return
            return -1
