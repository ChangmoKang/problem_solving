import sys
sys.stdin = open('input/12761.txt')


def bfs():
    q = [N]
    cnt = 0
    while q:
        cnt += 1
        qs, q = q, []
        for start in qs:
            goals = [
                start - 1,
                start + 1,
                start - A,
                start + A,
                start - B,
                start + B,
                start * A,
                start * B
            ]
            for goal in goals:
                if L <= goal <= R and not visited[goal]:
                    if goal == M:
                        return cnt
                    visited[goal] = 1
                    q.append(goal)


L, R = 0, 100000
A, B, N, M = map(int, input().split())

visited = [0]*(R + 1)
visited[N] = 1

print(bfs())
