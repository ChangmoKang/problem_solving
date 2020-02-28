from collections import deque

def solution(n,signs):
    def bfs(start_v):
        visited = [0]*n
        
        q = deque([start_v])
        while q:
            curr_v = q.popleft()
            for next_v in signs[curr_v]:
                if not visited[next_v]:
                    visited[next_v] = 1
                    q.append(next_v)
        return visited


    signs = [[i for i, s in enumerate(sign) if s] for sign in signs]

    return [bfs(v) for v in range(n)]
