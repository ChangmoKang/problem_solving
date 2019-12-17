import sys
sys.stdin = open('input/1389.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
rel = [[0]*N for _ in range(N)]

for _ in range(K):
    f, t = map(int, input().split())
    rel[f - 1][t - 1] = 1
    rel[t - 1][f - 1] = 1

scores = [-1]*N

for start in range(N):
    visited = [0]*N
    visited_score = 1
    visited[start] = visited_score
    q = [index for index in range(N) if rel[start][index]]
    while q:
        qs, q = q, []
        for target in qs:
            if not visited[target]:
                visited[target] = visited_score
                q.extend([index for index in range(N) if rel[target][index]])
        visited_score += 1
    scores[start] = sum(visited) - 1
print(scores.index(min(scores)) + 1)
