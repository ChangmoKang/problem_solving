import sys
sys.stdin = open('input/1219.txt')


def bfs():
    visited = [0]*100
    visited[0] = 1

    q = [0]
    while q:
        qs, q = q, []
        for f in qs:
            for t in adj[f]:
                if t == 99:
                    return 1
                if not visited[t]:
                    visited[t] = 1
                    q.append(t)
    return 0


for _ in range(10):
    tc, K = map(int, input().split())
    edge = list(map(int, input().split()))
    adj = [[] for _ in range(100)]

    for i in range(0, K * 2, 2):
        adj[edge[i]].append(edge[i + 1])

    print(f"#{tc} {bfs()}")
