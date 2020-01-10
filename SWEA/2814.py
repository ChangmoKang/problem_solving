import sys
sys.stdin = open('input/2814.txt')


def dfs(count, start):
    global result
    if count > result:
        result = count
    for to in range(1, N + 1):
        if adj[start][to] and not visited[to]:
            visited[to] = 1
            dfs(count + 1, to)
            visited[to] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj = [[0]*(N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    
    result = 0
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        visited[i] = 1
        dfs(1, i)
        visited[i] = 0

    print(f"#{tc} {result}")
