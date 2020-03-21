from collections import deque

COST = 2
def solution(n, costs):
    def bfs(start):
        nonlocal conn
        
        visited = [False]*n
        visited[start] = True
        
        q = deque([start])
        
        while q:
            a = q.popleft()
            for b in adj[a]:
                if not visited[b]:
                    visited[b] = True
                    q.append(b)
        
        conn = {i for i, flag in enumerate(visited) if flag}
        
        return sum(visited) == n


    costs.sort(key=lambda x:x[COST])
    
    adj = [set() for _ in range(n)]
    
    answer = 0
    conn = set()
    
    for f, t, c in costs:
        if f in conn and t in conn:
            continue

        adj[f].add(t)
        adj[t].add(f)

        answer += c
        
        if bfs(f):
            return answer
