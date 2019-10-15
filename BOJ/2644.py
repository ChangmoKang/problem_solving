import sys
sys.stdin = open('input/2644.txt')

def bfs(v):
    visited = [1] + [0]*N
    visited[v] = 1
    q = [v]
    cnt = 0
    while q:
        cnt += 1
        contents, q = q, []
        for vv in contents:
            for v in dic[vv]:
                if v == to_idx:
                    return cnt
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
    return -1

N = int(input())
from_idx, to_idx = map(int, input().split())
K = int(input())

dic = {}
for _ in range(K):
    p, c = map(int, input().split())
    if p not in dic:
        dic[p] = [c]
    else:
        dic[p].append(c)

    if c not in dic:
        dic[c] = [p]
    else:
        dic[c].append(p)

print(bfs(from_idx))
