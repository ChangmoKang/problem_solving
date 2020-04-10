from itertools import product
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def solution(land, height):
    def get_parent(x):
        if parent[x] == x:
            return x

        parent[x] = get_parent(parent[x])
        return parent[x]


    def union_parent(a, b):
        a = get_parent(a)
        b = get_parent(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b


    def find_parent(a, b):
        a = get_parent(a)
        b = get_parent(b)

        return True if a == b else False
    

    N = len(land)
    visited = [[0]*N for _ in range(N)]
    
    num = 0
    for i, j in product(range(N), range(N)):
        if not visited[i][j]:
            num += 1
            visited[i][j] = num
            q = deque([[i, j]])
            
            while q:
                r, c = q.popleft()
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and abs(land[r][c] - land[rr][cc]) <= height:
                        visited[rr][cc] = num
                        q.append([rr, cc])

    if num == 1:
        return 0
    
    adj = {}
    
    for r, c in product(range(N), range(N)):
        for x in range(4):
            rr, cc = r + dr[x], c + dc[x]
            if 0 <= rr < N and 0 <= cc < N and visited[r][c] != visited[rr][cc]:
                a, b = visited[r][c], visited[rr][cc]
                cost = abs(land[r][c] - land[rr][cc])
                
                if a > b:
                    if (b, a) not in adj:
                        adj[b, a] = cost
                    else:
                        if cost < adj[b, a]:
                            adj[b, a] = cost
                else:
                    if (a, b) not in adj:
                        adj[a, b] = cost
                    else:
                        if cost < adj[a, b]:
                            adj[a, b] = cost
    
    edge = []
    for node, cost in adj.items():
        edge.append([node[0], node[1], cost])
        
    edge.sort(key=lambda x:x[2])
    
    parent = list(range(num + 1))
    
    cnt = 0
    result = 0
    for a, b, v in edge:
        if cnt == num - 1:
            break

        if not find_parent(a, b):
            result += v
            union_parent(a, b)
            cnt += 1
    
    return result
    