import sys
sys.stdin = open('input/1260.txt')


def dfs(start):
    for key in dic[start]:
        if not visited[key]:
            visited[key] = 1
            result.append(key)
            dfs(key)


def bfs(start):
    q = [start]
    while q:
        e = q.pop(0)
        for key in dic[e]:
            if not visited[key]:
                visited[key] = 1
                result.append(key)
                q.append(key)


for tc in range(1, int(input()) + 1):
    N, M, S = map(int, input().split())

    dic = {}
    for _ in range(M):
        s, g = map(int, input().split())
        if s not in dic:
            dic[s] = [g]
        else:
            dic[s].append(g)

        if g not in dic:
            dic[g] = [s]
        else:
            dic[g].append(s)

    for key in dic:
        dic[key].sort()

    if S in dic:
        for k in range(2):
            visited = [0]*(N+1)
            visited[S] = 1
            result = [S]
            if k == 0:
                dfs(S)
            else:
                bfs(S)

            print(*result)
    else:
        print(S)
        print(S)
