import sys
sys.stdin = open('input/18227.txt')
input = sys.stdin.readline


def bfs():
    visited = [0] * (N + 1)
    visited[C] = 1
    q = [C]
    depth = 1
    table = [[None, depth] for _ in range(N + 1)]
    while q:
        depth += 1
        qs, q = q, []
        for vertex in qs:
            for target in adj[vertex]:
                if not visited[target]:
                    visited[target] = 1
                    q.append(target)
                    table[target][0] = vertex
                    table[target][1] = depth
    return table


N, C = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    f, t = map(int, input().split())
    adj[f].append(t)
    adj[t].append(f)

table = bfs()

result = []
tank = [0] * (N + 1)

cases = [list(map(int, input().split())) for _ in range(int(input()))]
dic = {}
for method, v in cases:
    if method == 1:
        if v not in dic:
            dic[v] = 1
        else:
            dic[v] += 1
    else:
        for key in dic:
            target = key
            while True:
                if table[target][0] == None:
                    tank[target] += dic[key]
                    break
                else:
                    tank[target] += dic[key]
                    target = table[target][0]
        result.append(str(tank[v] * table[v][1]))
        dic = {}

print("\n".join(result))
