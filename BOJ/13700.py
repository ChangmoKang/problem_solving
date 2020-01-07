import sys
sys.stdin = open('input/13700.txt')


def bfs():
    visited = [0]*N
    visited[S] = 1

    q = [S]
    time = 0
    while q:
        time += 1
        qs, q = q, []
        for location in qs:
            for x in range(2):
                new_location = location + d[x]
                if 0 <= new_location < N and board[new_location] and not visited[new_location]:
                    if new_location == G:
                        return time
                    visited[new_location] = 1
                    q.append(new_location)
    return "BUG FOUND"


N, S, G, F, B, K = map(int, input().split())
S, G = S - 1, G - 1
d = [F, -B]

board = [1]*N
if K:
    for police in map(int, input().split()):
        board[police - 1] = 0

print(bfs())
