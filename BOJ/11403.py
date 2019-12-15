import sys
sys.stdin = open('input/11403.txt')


def bfs(q):
    visited = [0]*N
    while q:
        qs, q = q, []
        for f in qs:
            if not visited[f]:
                visited[f] = 1
                adj[FROM][f] = 1
                q.extend([t for t in range(N) if not visited[t] and graph[f][t]])


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
adj = [[0]*N for _ in range(N)]

for FROM in range(N):
    bfs([TO for TO in range(N) if graph[FROM][TO]])

for x in range(N):
    print(*adj[x])
