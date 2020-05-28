import sys
from collections import deque
sys.stdin = open('input/9205.txt')


def bfs(start):
    q = deque([start])

    while q:
        target = q.popleft()

        for next, elem in enumerate(adj[target]):
            if elem and not visited[next]:
                visited[next] = True
                if next == N - 1:
                    return 'happy'
                q.append(next)
    return 'sad'


def calc(v1, v2):
    return abs(v1[1] - v2[1]) + abs(v1[0] - v2[0])


for _ in range(int(input())):
    N = int(input()) + 2
    v = [list(map(int, input().split())) for _ in range(N)]

    adj = [[False]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and calc(v[i], v[j]) <= 1000:
                adj[i][j] = True

    visited = [False]*(N)
    visited[0] = True

    if adj[0][-1]:
        print('happy')
    else:
        print(bfs(0))

        """
        # Floyd–Warshall algorithm
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if adj[i][k] and adj[k][j]:
                        adj[i][j] = True

        if adj[0][-1]:
            print('happy')
        else:
            print('sad')
        """
