from collections import deque

ROUTE = 1
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(maps):
    N, M = len(maps), len(maps[0])
    
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    
    q = deque([[0, 0]])
    while q:
        r, c = q.popleft()
        
        for dr, dc in DELTAS:
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and maps[next_r][next_c] == ROUTE:
                visited[next_r][next_c] = visited[r][c] + 1
                if (next_r, next_c) == (N - 1, M - 1):
                    return visited[next_r][next_c]
                q.append([next_r, next_c])
    return -1
