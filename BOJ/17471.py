import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input/17471.txt')


def bfs(team):
    q = deque([team[0]])
    visited = [True] + [False if w in team else True for w in range(1, N + 1)]
    visited[team[0]] = True

    while q:
        f = q.popleft()
        for t in adj[f]:
            if not visited[t]:
                visited[t] = True
                q.append(t)
    
    return True if sum(visited) == N + 1 else False


N = int(input())
po = [None] + list(map(int, input().split()))
adj = [None]
for i in range(N):
    adj.append(list(map(int, input().split()))[1:])

result = float('inf')
for k in range(1, N//2 + 1):
    for team_a in combinations(range(1, N + 1), k):
        team_b = tuple(set(range(1, N + 1)) - set(team_a))
        if bfs(team_a) and bfs(team_b):
            result_a = sum(po[w] for w in range(1, N + 1) if w in team_a)
            result_b = sum(po[w] for w in range(1, N + 1) if w in team_b)
            if result > abs(result_a - result_b):
                result = abs(result_a - result_b)

print(result) if result != float('inf') else print(-1)
