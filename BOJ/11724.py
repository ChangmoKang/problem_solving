import sys
sys.stdin = open('input/11724.txt')


N, K = map(int, input().split())
graph = [[] for _ in range(N)]

visited = {}
for _ in range(K):
    f, t = map(int, input().split())
    graph[f - 1].append(t - 1)
    graph[t - 1].append(f - 1)
    visited[f - 1] = 0
    visited[t - 1] = 0

result = N - len(visited)
for f in visited:
    if not visited[f]:
        visited[f] = 1
        q = graph[f]
        while q:
            qs, q = q, []
            for n_f in qs:
                if not visited[n_f]:
                    visited[n_f] = 1
                    if graph[n_f]:
                        q.extend(graph[n_f])
        result += 1
print(result)
